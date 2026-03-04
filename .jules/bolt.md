## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-03-05 - [Context Building Performance Optimization]
**Learning:** During progressive context loading and summary generation in the `AgentLoop`, `SkillsLoader` was continuously parsing YAML frontmatter, decoding JSON nanobot metadata, reading files from disk, and issuing numerous system calls for `shutil.which` to check system requirements, causing excessive disk I/O and repetitive parsing overhead per loop iteration.
**Action:** Implemented an in-memory `_file_cache` mapping file paths to their last modification time (`os.path.getmtime`), skipping reads and string parsing entirely if the file hasn't changed. Added a similar `_which_cache` to short-circuit repetitive binary lookups in the `$PATH`.
