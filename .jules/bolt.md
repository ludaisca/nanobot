## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-13 - [String Case Conversion Optimization]
**Learning:** In Python, string operations like case conversion can be heavily optimized by adding simple fast-paths (e.g., checking `islower()` or `_ in name` before processing). Furthermore, using a pre-compiled regex for camel-to-snake conversion is significantly faster (~35%) than character-by-character iteration. For snake-to-camel, using a list comprehension inside `"".join()` instead of a generator expression eliminates generator overhead, improving performance.
**Action:** Always consider fast-paths for string operations that might already be in the target format, and prefer list comprehensions over generator expressions inside `"".join()` for small lists. Profile micro-optimizations carefully before applying.
