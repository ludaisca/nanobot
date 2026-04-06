## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-12 - [Python String Conversions]
**Learning:** When optimizing Python string operations (like camelCase to snake_case conversions), per-character iteration is slow. Pre-compiled regular expressions (like `re.compile(r'(?<!^)(?=[A-Z])')`) with `re.sub` are significantly faster. Additionally, adding simple fast-paths (like checking `islower()` or `_ not in name`) to skip processing altogether provides drastic speed improvements for already-formatted strings. For aggregations, list comprehensions inside `"".join()` are noticeably faster than generator expressions.
**Action:** When implementing repetitive string formatting utilities, prioritize pre-compiled regexes over manual character iteration, always use list comprehensions in `join()`, and add O(1) checks to short-circuit processing on unmodified input.
