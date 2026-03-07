import time
from pathlib import Path
from nanobot.agent.context import ContextBuilder
from nanobot.agent.skills import SkillsLoader

def test_perf():
    workspace = Path(".")
    builder = ContextBuilder(workspace)

    # Run once to warm up any disk caches
    builder.build_system_prompt()

    start = time.perf_counter()
    for _ in range(100):
        builder.build_system_prompt()
    end = time.perf_counter()

    print(f"Time for 100 builds: {end - start:.4f}s")

if __name__ == "__main__":
    test_perf()
