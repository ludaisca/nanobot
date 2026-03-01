## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2025-03-01 - [Cache SKILL.md file access in SkillsLoader]
**Learning:** `ContextBuilder.build_system_prompt` executes `SkillsLoader` methods repeatedly on each agent loop cycle, parsing `SKILL.md` frontmatter and accessing the filesystem to load all skills. Due to `os.stat` calls and regex processing overhead on multiple large files, this creates a significant performance bottleneck.
**Action:** Implement an in-memory dictionary `_file_cache` within `SkillsLoader` that stores parsed file contents and metadata, using `os.stat().st_mtime` to lazily invalidate cache entries when files are modified. This avoids unnecessary reads and frontmatter parsing during regular prompt generation while remaining responsive to workspace edits.
