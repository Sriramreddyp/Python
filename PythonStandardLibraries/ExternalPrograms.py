import subprocess

# completed = subprocess.run(["dir"], shell=True, capture_output=True,text=True)
completed = subprocess.run(["python3", "CallBackScript.py"],
                           shell=True, capture_output=True, text=True)
print("args", completed.args)
print("returnCode", completed.returncode)
print("strerr", completed.stderr)
print("stdout", completed.stdout)
