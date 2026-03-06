## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-03-06 - [Context Build Performance]
**Learning:** During system prompt building, repeated calls to check availability (`shutil.which`) and load skill contents (`SKILL.md`) caused extreme performance degradation.
**Action:** Caching both `mtime` based file reads and `shutil.which` results directly in memory saves substantial disk I/O when progressively loading features across a large suite of capabilities.
