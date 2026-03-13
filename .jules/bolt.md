## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-12 - [SkillsLoader File Caching]
**Learning:** Missing caching on frequently accessed metadata files (like `SKILL.md` where the application loops over them multiple times during startup and summarization) can cause significant redundant disk I/O.
**Action:** Always add an in-memory cache (checking `os.path.getmtime` for invalidation) when frequently reading static or rarely changing configuration/metadata files from disk.
