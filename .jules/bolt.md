## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.
## 2024-02-12 - [Python String Reallocation Bottleneck]
**Learning:** During recursive dictionary conversions (`convert_keys`), character-by-character string building and list joins create significant object reallocation overhead in Python. Pre-compiled Regex (`re.sub`) with fast-paths is up to 10x faster for bulk string parsing.
**Action:** When finding string manipulation inside tight loops or recursive descents, look for opportunities to replace manual parsing with C-backed Python builtins like `re` and `str.islower()`.
