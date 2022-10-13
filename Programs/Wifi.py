import subprocess

data = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"]).decode('utf-8').split("\n")  # Take Out data of everyProfile sperated by a line break

profiles = [i.split(":")[1][1:-1]
            for i in data if "All User Profile" in i]  # Store Profile Usernames


for i in profiles:
    # try:
    results = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode("utf-8").split("\n")  # Store outputs of this particular command
    # except subprocess.SubprocessError:
    #     print("Command Not Executed")
    results = [b.split(":")[1][1:-1]
               for b in results if "Key Content" in b]  # Extrack passwords

    try:
        print("{:<30}    |  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}    |  {:<}".format(i, "Not Found"))
