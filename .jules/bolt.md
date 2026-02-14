## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-14 - [Session Save Optimization]
**Learning:** Optimizing session saving by appending to JSONL files (instead of full rewrite) yields massive (~22x) speedups but introduces correctness risks if memory state diverges from disk (e.g., via edits). A lightweight safety check (comparing tail content) can guard against this without sacrificing performance for the common append-only case. Also, relying on file `mtime` for metadata is robust when file headers cannot be cheaply updated.
**Action:** When optimizing I/O with append-only strategies, always validate the "append-only" assumption with a cheap runtime check (e.g., tail hash/content) and handle metadata updates gracefully (e.g., via filesystem stats).
