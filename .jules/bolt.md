## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-15 - [File System Cache in Context Builder]
**Learning:** Repetitive disk I/O in the context building pipeline (specifically reading `SKILL.md` files and running `shutil.which` during the `AgentLoop`) causes significant latency overhead, especially when checking requirements for many skills in parallel or repeatedly on every message.
**Action:** Cache the content of frequently accessed metadata/skills files using an in-memory dictionary checked against `os.path.getmtime`. Cache CLI requirements with a simple `shutil.which` result map.