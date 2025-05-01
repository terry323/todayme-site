import os
import subprocess
import time

def run():
    repo_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_path)
    subprocess.call("git pull", shell=True)
    subprocess.call("git add .", shell=True)
    subprocess.call("git commit -m \"auto: create/update subdomain\"", shell=True)
    subprocess.call("git push origin main", shell=True)
    with open("executions/last_run.log", "w") as f:
        f.write(f"Last run: {time.ctime()}\n")

if __name__ == "__main__":
    run()