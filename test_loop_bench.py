import pytest
import asyncio
from pathlib import Path
from nanobot.agent.context import ContextBuilder
from nanobot.agent.skills import SkillsLoader

def test_skills_loader(benchmark):
    workspace = Path("/tmp/nanobot_bench_skills")
    import shutil
    if workspace.exists():
        shutil.rmtree(workspace)
    workspace.mkdir(exist_ok=True)

    skills_dir = workspace / "skills"
    skills_dir.mkdir(exist_ok=True)

    # Create 50 dummy skills
    for i in range(50):
        skill_dir = skills_dir / f"skill_{i}"
        skill_dir.mkdir(exist_ok=True)
        with open(skill_dir / "SKILL.md", "w") as f:
            f.write(f"---\ndescription: 'Dummy skill {i}'\n---\n\n# Skill {i}\n\nContent for skill {i}")

    loader = SkillsLoader(workspace)

    # We'll benchmark get_always_skills, list_skills, build_skills_summary which simulate an agent context build
    def bench_run():
        loader.get_always_skills()
        loader.build_skills_summary()

    benchmark(bench_run)
    shutil.rmtree(workspace)
