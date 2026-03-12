## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-12 - [Redundant Context I/O]
**Learning:** Repetitive disk reads during context building drastically compound latency in high-frequency loops. Caching file contents with an `os.path.getmtime` check proved critical in the skills loader. However, memoizing `shutil.which` results introduced a functional regression, breaking the agent's ability to dynamically unlock skills when it successfully installs missing dependencies.
**Action:** Always implement time-based or change-aware caching for files (like Markdown skills or configs) that are read frequently. Avoid permanently caching stateful environment queries (like `shutil.which`) in long-lived components unless there is a clear invalidation strategy.
