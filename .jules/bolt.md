## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-13 - [Skill File Caching Optimization]
**Learning:** Caching files that define agent capabilities (`SKILL.md`) saves disk I/O on hot paths, but you cannot permanently cache `shutil.which` availability checks. The agent loop must re-check requirements dynamically so it can install dependencies on the fly and immediately unlock new skills.
**Action:** When adding memory caches for dynamic plugins or skills, separate the static data (file content cached by `mtime`) from the dynamic environment state (CLI tool availability checks).
