## 2026-02-12 - [Async Memory Consolidation]
**Learning:** Moving heavy LLM operations (like memory consolidation) to background tasks requires careful handling of shared mutable state (sessions). Using an offset-based approach for trimming (`messages[n_removed:]`) is safer than negative slicing (`messages[-keep:]`) when the list can grow concurrently. Also, always track background tasks in a set to prevent garbage collection.
**Action:** When optimizing long-running operations in async loops, always ensure state consistency and task lifecycle management.

## 2024-05-23 - [SkillsLoader Context Building Bottleneck]
**Learning:** In the hot path of building system prompts (`ContextBuilder.build_system_prompt`), `SkillsLoader` repeatedly loads and parses the `SKILL.md` markdown files and their pseudo-YAML frontmatter. This frequent, redundant I/O and regex evaluation significantly impacts performance, but caching MUST be done carefully (`st_mtime`-based) so that dynamically installed binaries or edited markdown files are immediately reflected in the capabilities, while skipping the cache for runtime checks like `shutil.which`.
**Action:** When parsing static or mostly-static configuration files inside an agent's inner loop, use `st_mtime`-based caching for file content and metadata parsing, but keep environment checks (like binary availability) strictly dynamic and un-cached.
