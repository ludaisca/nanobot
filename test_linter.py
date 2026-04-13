import subprocess

def run():
    subprocess.run(["ruff", "check", "nanobot/agent/skills.py"], check=False)

if __name__ == "__main__":
    run()
