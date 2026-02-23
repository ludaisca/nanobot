## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-12 - [Synchronous Context Building]
**Learning:** `ContextBuilder` synchronously reads bootstrap files (AGENTS.md, etc.) and memory on every message loop iteration, causing unnecessary blocking I/O even when files haven't changed.
**Action:** Implement file content caching using `st_mtime` to avoid redundant reads in high-frequency loops.
