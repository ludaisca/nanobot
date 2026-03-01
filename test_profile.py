import cProfile
import pstats
import io
from pathlib import Path
from nanobot.agent.skills import SkillsLoader

workspace = Path("/tmp/nanobot_profile_skills")
import shutil
if workspace.exists():
    shutil.rmtree(workspace)
workspace.mkdir(exist_ok=True)

skills_dir = workspace / "skills"
skills_dir.mkdir(exist_ok=True)

for i in range(100):
    skill_dir = skills_dir / f"skill_{i}"
    skill_dir.mkdir(exist_ok=True)
    with open(skill_dir / "SKILL.md", "w") as f:
        f.write(f"---\ndescription: 'Dummy skill {i}'\n---\n\n# Skill {i}\n\nContent for skill {i}")

loader = SkillsLoader(workspace)

pr = cProfile.Profile()
pr.enable()

for _ in range(10):  # Simulate 10 iterations of agent loop
    loader.get_always_skills()
    loader.build_skills_summary()

pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats(20)
print(s.getvalue())
