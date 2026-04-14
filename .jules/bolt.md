## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## $(date +%Y-%m-%d) - [SkillsLoader Caching]
**Learning:** SkillsLoader was repeatedly reading SKILL.md files from disk on every invocation, causing significant overhead when listing or building summaries. Caching by checking `st_mtime` correctly avoids redundant I/O while ensuring the cache invalidates automatically if files change.
**Action:** Always check file I/O operations in loops for caching opportunities.
