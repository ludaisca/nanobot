## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2025-02-12 - [Context Building Performance Optimization]
**Learning:** During continuous agent interaction loops, static file content (like SKILL.md) and environmental checks (`shutil.which` for PATH resolution) are unnecessarily re-evaluated for every message processing cycle. This leads to substantial repetitive I/O, especially when evaluating multiple tools and their constraints repeatedly in large directories.
**Action:** Implemented caching strategies to store `mtime` for file contents and boolean outcomes for `shutil.which` lookups. This should significantly speed up processing in iterative chat scenarios by caching repetitive environment and disk inspections. When writing context builders, persist these caches in memory.
