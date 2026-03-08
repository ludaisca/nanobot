## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-12 - [SkillsLoader Disk I/O Bottleneck]
**Learning:** `SkillsLoader` parses all skills and checks requirements using `shutil.which` multiple times during context building (e.g. `list_skills`, `load_skill`). This causes excessive disk I/O when processing multiple requests.
**Action:** Use an in-memory cache for file contents checking `os.path.getmtime`. For `shutil.which` calls, cache only `True` results to avoid breaking dynamic dependency installation where an initially missing tool might be installed during the process.
