"""Session management for conversation history."""

import json
import os
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from loguru import logger

from nanobot.utils.helpers import ensure_dir, safe_filename


@dataclass
class Session:
    """
    A conversation session.

    Stores messages in JSONL format for easy reading and persistence.
    """

    key: str  # channel:chat_id
    messages: list[dict[str, Any]] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    metadata: dict[str, Any] = field(default_factory=dict)

    # Internal tracking for incremental saves
    _persisted_count: int = field(default=0, init=False)

    def add_message(self, role: str, content: str, **kwargs: Any) -> None:
        """Add a message to the session."""
        msg = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            **kwargs
        }
        self.messages.append(msg)
        self.updated_at = datetime.now()

    def get_history(self, max_messages: int = 50) -> list[dict[str, Any]]:
        """
        Get message history for LLM context.

        Args:
            max_messages: Maximum messages to return.

        Returns:
            List of messages in LLM format.
        """
        # Get recent messages
        recent = self.messages[-max_messages:] if len(self.messages) > max_messages else self.messages

        # Convert to LLM format (just role and content)
        return [{"role": m["role"], "content": m["content"]} for m in recent]

    def clear(self) -> None:
        """Clear all messages in the session."""
        self.messages = []
        self.updated_at = datetime.now()


class SessionManager:
    """
    Manages conversation sessions.

    Sessions are stored as JSONL files in the sessions directory.
    """

    def __init__(self, workspace: Path):
        self.workspace = workspace
        self.sessions_dir = ensure_dir(Path.home() / ".nanobot" / "sessions")
        self._cache: dict[str, Session] = {}

    def _get_session_path(self, key: str) -> Path:
        """Get the file path for a session."""
        safe_key = safe_filename(key.replace(":", "_"))
        return self.sessions_dir / f"{safe_key}.jsonl"

    def get_or_create(self, key: str) -> Session:
        """
        Get an existing session or create a new one.

        Args:
            key: Session key (usually channel:chat_id).

        Returns:
            The session.
        """
        # Check cache
        if key in self._cache:
            return self._cache[key]

        # Try to load from disk
        session = self._load(key)
        if session is None:
            session = Session(key=key)

        self._cache[key] = session
        return session

    def _load(self, key: str) -> Session | None:
        """Load a session from disk."""
        path = self._get_session_path(key)

        if not path.exists():
            return None

        try:
            messages = []
            metadata = {}
            created_at = None

            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    data = json.loads(line)

                    if data.get("_type") == "metadata":
                        metadata = data.get("metadata", {})
                        created_at = datetime.fromisoformat(data["created_at"]) if data.get("created_at") else None
                    else:
                        messages.append(data)

            session = Session(
                key=key,
                messages=messages,
                created_at=created_at or datetime.now(),
                metadata=metadata
            )
            session._persisted_count = len(messages)
            return session
        except Exception as e:
            logger.warning(f"Failed to load session {key}: {e}")
            return None

    def save(self, session: Session) -> None:
        """Save a session to disk."""
        path = self._get_session_path(session.key)

        # Check if we can append: file exists and we have only added messages.
        # NOTE: This assumes messages are append-only and immutable once added.
        # If messages are modified in-place without changing length, this logic
        # will fail to persist changes. nanobot architecture treats session messages
        # as an append-only log, so this is safe.
        can_append = (
            path.exists() and
            len(session.messages) >= session._persisted_count
        )

        # If we have 0 persisted, we might be creating the file or rewriting empty.
        # If path exists but persisted is 0, it means we loaded it or it's a new object for existing file?
        # If we loaded it, persisted_count would be set.
        # If we created new object for existing file (race?), persisted_count is 0.
        # We should be careful not to append duplicate messages if persisted_count is wrong.
        # But _load sets persisted_count.
        # get_or_create -> _load.

        if can_append and session._persisted_count > 0:
            new_messages = session.messages[session._persisted_count:]
            if new_messages:
                with open(path, "a") as f:
                    for msg in new_messages:
                        f.write(json.dumps(msg) + "\n")
        else:
            # Full rewrite (new file, or messages removed/reordered)
            with open(path, "w") as f:
                # Write metadata first
                metadata_line = {
                    "_type": "metadata",
                    "created_at": session.created_at.isoformat(),
                    "updated_at": session.updated_at.isoformat(),
                    "metadata": session.metadata
                }
                f.write(json.dumps(metadata_line) + "\n")

                # Write messages
                for msg in session.messages:
                    f.write(json.dumps(msg) + "\n")

        session._persisted_count = len(session.messages)
        self._cache[session.key] = session

    def delete(self, key: str) -> bool:
        """
        Delete a session.

        Args:
            key: Session key.

        Returns:
            True if deleted, False if not found.
        """
        # Remove from cache
        self._cache.pop(key, None)

        # Remove file
        path = self._get_session_path(key)
        if path.exists():
            path.unlink()
            return True
        return False

    def list_sessions(self) -> list[dict[str, Any]]:
        """
        List all sessions.

        Returns:
            List of session info dicts.
        """
        cache_path = self.sessions_dir / ".sessions_metadata.json"
        cache = {}
        if cache_path.exists():
            try:
                with open(cache_path) as f:
                    cache = json.load(f)
            except Exception:
                pass

        sessions = []
        updated_cache = {}
        cache_changed = False

        for entry in os.scandir(self.sessions_dir):
            if not entry.is_file() or not entry.name.endswith(".jsonl"):
                continue

            mtime = entry.stat().st_mtime
            cached_entry = cache.get(entry.name)

            if cached_entry and cached_entry.get("mtime") == mtime:
                session_info = cached_entry["data"]
                sessions.append(session_info)
                updated_cache[entry.name] = cached_entry
            else:
                try:
                    path = Path(entry.path)
                    # Read just the metadata line
                    with open(path) as f:
                        first_line = f.readline().strip()
                        if first_line:
                            data = json.loads(first_line)
                            if data.get("_type") == "metadata":
                                # Use mtime for updated_at to reflect append-only updates
                                updated_at_iso = datetime.fromtimestamp(mtime).isoformat()
                                session_info = {
                                    "key": path.stem.replace("_", ":"),
                                    "created_at": data.get("created_at"),
                                    "updated_at": updated_at_iso,
                                    "path": str(path)
                                }
                                sessions.append(session_info)
                                updated_cache[entry.name] = {
                                    "mtime": mtime,
                                    "data": session_info
                                }
                                cache_changed = True
                except Exception:
                    continue

        if len(updated_cache) != len(cache):
            cache_changed = True

        if cache_changed:
            try:
                with open(cache_path, "w") as f:
                    json.dump(updated_cache, f)
            except Exception:
                pass

        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)
