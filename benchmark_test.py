import pytest
from pathlib import Path
from nanobot.agent.context import ContextBuilder

def test_context_building(benchmark):
    # Setup
    workspace = Path("/tmp/nanobot_bench")
    workspace.mkdir(exist_ok=True)
    (workspace / "skills").mkdir(exist_ok=True)

    # Create some dummy skills
    for i in range(10):
        skill_dir = workspace / "skills" / f"skill_{i}"
        skill_dir.mkdir(exist_ok=True)
        with open(skill_dir / "SKILL.md", "w") as f:
            f.write(f"---\ndescription: 'Dummy skill {i}'\n---\n\n# Skill {i}\n\nContent for skill {i}")

    # Create some dummy memory
    memory_dir = workspace / "memory"
    memory_dir.mkdir(exist_ok=True)
    with open(memory_dir / "MEMORY.md", "w") as f:
        f.write("# Memory\n\nSome dummy memory content " * 100)
    with open(memory_dir / "HISTORY.md", "w") as f:
        f.write("# History\n\nSome dummy history content " * 100)

    # Create dummy bootstrap files
    for f in ContextBuilder.BOOTSTRAP_FILES:
        with open(workspace / f, "w") as fp:
            fp.write(f"# {f}\n\nContent for {f}")

    builder = ContextBuilder(workspace)

    # Benchmark
    result = benchmark(builder.build_system_prompt)

    # Cleanup
    import shutil
    shutil.rmtree(workspace)

    assert result
