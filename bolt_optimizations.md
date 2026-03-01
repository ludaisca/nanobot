## Potential Optimizations Found

1. `SkillsLoader` parses SKILL.md multiple times for the same skills.
   - `get_skill_metadata` calls `load_skill` and does regex parsing.
   - Profile shows `get_skill_metadata`, `load_skill`, `list_skills`, `_get_skill_meta`, `_get_skill_description` taking up significant time, doing repeated disk I/O `posix.stat`, `open`, `read_text`.
   - The memory system prompt confirms this is an issue: "Context building (`ContextBuilder.build_system_prompt`) is a performance-critical path as it triggers `SkillsLoader` methods repeatedly; caching in `SkillsLoader` is essential to minimize disk I/O."
   - AND memory explicitly says: "The `SkillsLoader` (`nanobot/agent/skills.py`) implements an in-memory `_file_cache` (keyed by path) to store file content, invalidating entries based on `st_mtime` to optimize repeated reads of `SKILL.md` files."

Wait, let's look at `nanobot/agent/skills.py` again. Is there a `_file_cache` implemented?
