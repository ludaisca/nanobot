## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-12 - [SkillsLoader Caching]
**Learning:** `ContextBuilder` reconstructs the system prompt on every message, which recursively loads skills. `SkillsLoader` was hitting the disk and parsing YAML for every skill on every prompt build, creating an O(N*M) bottleneck where N is skills and M is messages.
**Action:** Implemented an `mtime`-based cache for skill content and metadata. This reduces I/O from linear to constant (cached) and avoids repetitive parsing. Always check for repetitive I/O in hot paths like prompt construction.
