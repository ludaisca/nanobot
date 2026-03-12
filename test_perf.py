import time
from pathlib import Path

from nanobot.agent.skills import SkillsLoader

loader = SkillsLoader(Path("workspace"))
start = time.time()
for _ in range(100):
    loader.list_skills()
    loader.build_skills_summary()
end = time.time()
print(f"Time taken: {end - start:.4f}s")
