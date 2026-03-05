## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-03-05 - [Context Building Performance Optimization]
**Learning:** Repetitive parsing of Markdown and frontmatter during the agent loop context building causes significant overhead (thousands of calls per loop) due to file I/O operations and shell checks (`shutil.which()`).
**Action:** Implemented an in-memory `_file_cache` leveraging `os.path.getmtime` and a `_which_cache` to drastically reduce redundant parsing and system calls. Always ensure repeated filesystem queries in tight loops are cached properly while maintaining cache invalidation logic.
