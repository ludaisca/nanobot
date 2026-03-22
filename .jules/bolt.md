## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2026-02-28 - [Cache File Reads on LLM Hot Path]
**Learning:** In the `AgentLoop`, loading skill summaries repeatedly hits the disk (`path.read_text()`) for every message because `SkillsLoader` parses the SKILL.md frontmatter each time to determine capabilities. Disk I/O during the core loop context building severely impacts responsiveness. However, caching the full file content permanently risks breaking the agent if a new skill is written or dependencies change dynamically.
**Action:** When building text representations of files iteratively on a hot path, use an `st_mtime`-based in-memory cache to skip redundant disk reads without sacrificing dynamic reactivity.
