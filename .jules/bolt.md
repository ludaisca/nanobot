## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-03-16 - [Concurrent Tool Execution]
**Learning:** Sequential execution of multiple tool calls from a single LLM response acts as a significant bottleneck, especially for I/O-bound operations (like reading files or doing web searches). Running them concurrently reduces the total execution time to the time taken by the slowest single tool execution.
**Action:** Always use `asyncio.gather` to execute multiple independent tool calls returned in an LLM response simultaneously instead of looping over them with `await` sequentially.
