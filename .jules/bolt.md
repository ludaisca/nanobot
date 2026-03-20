## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-03-20 - [SkillsLoader File Cache Optimization]
**Learning:** Frequent file access in high-throughput components like the `AgentLoop`'s skill evaluation slows down performance considerably. Caching file contents in memory (`_file_cache`) and only reading from disk when the file's modification time (`st_mtime`) changes significantly reduces disk I/O while maintaining responsiveness to file changes. It is crucial, however, to only cache file contents and NOT environment states like `shutil.which`, allowing dynamic installations to still unlock skills at runtime.
**Action:** When repeatedly reading configuration or capability files (like `SKILL.md`) within loops, use an in-memory cache validated by `st_mtime` to optimize performance without sacrificing dynamic updates.
