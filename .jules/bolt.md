## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2025-04-04 - [Config Loader String Optimization]
**Learning:** When optimizing Python string operations (like camelCase to snake_case conversions), pre-compiled regular expressions (`re.compile(r'(?<!^)(?=[A-Z])')`) and fast-paths (like checking `islower()` or `'_' not in name`) can significantly speed up execution.
**Action:** Always consider fast-paths and pre-compiled regexes for hot-path string manipulation functions, especially those used during configuration loading or serialization.
