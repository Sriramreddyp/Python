import subprocess

data = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"]).decode('utf-8').split("\n")

profiles = [i.split(":")[1][1:-1]
            for i in data if "All User Profile" in i]

# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]


for i in profiles:
    results = subprocess.run(
        ['netsh', 'wlan', 'show', 'profile', i, 'key=clear'], shell=True)
    # results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    # print(type(results))
