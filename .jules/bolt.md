## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-13 - [Parallel Tool Execution]
**Learning:** Sequential execution of multiple tool calls from a single LLM response is a significant bottleneck. Using `asyncio.gather` for parallel execution can drastically reduce latency (e.g., 3s -> 1s for 3 tasks). However, this assumes tool independence within a single turn, which is standard for function calling but could be a breaking change if models rely on side-effects of prior tools in the same list.
**Action:** When implementing parallel execution, always verify that the order of results and logs is preserved to maintain deterministic history and debugging.
