## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-12 - [Cache Skill File Contents]
**Learning:** Redundant disk I/O for `SKILL.md` files during agent execution can slow down the loop. In-memory caching with `st_mtime` checks is effective, but caching dynamic availability checks like `shutil.which` breaks runtime skill unlocking.
**Action:** When caching file reads for performance, always use `stat().st_mtime` to prevent stale reads, and carefully isolate static content from dynamic evaluation logic.
