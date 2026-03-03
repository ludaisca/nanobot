## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-03-03 - [Caching Disk and Process Lookups in Hot Paths]
**Learning:** During system prompt construction (`ContextBuilder.build_system_prompt`), repeating disk I/O for `SKILL.md` content and `shutil.which` availability checks can become a hidden bottleneck if there are multiple skills. Because this runs on every agent step, avoiding redundant OS calls significantly reduces context build time (reduced by ~50% in benchmarks).
**Action:** Always consider using in-memory mtime-based caches (`_file_cache`) and lookup caches (`_which_cache`) when repetitive disk or process checks are inside an application's hot path (like an LLM context builder loop).
