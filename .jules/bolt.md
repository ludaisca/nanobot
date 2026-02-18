## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-12 - [Session Persistence Optimization]
**Learning:** Optimizing `save` to be append-only (O(1)) requires careful state tracking (`_persisted_count`) to handle truncations/modifications safely. Crucially, if file headers store metadata (like `updated_at`), they become stale on append. Relying on file system attributes (`mtime`) for listing/sorting is more robust than reading potentially outdated file content.
**Action:** When implementing append-only optimizations, verify that read operations (like listing) don't rely on static headers that might not be updated during appends.
