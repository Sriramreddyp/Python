names = ["john", "mary"]
# found = False
for name in names:
    if name.startswith("z"):
        print('Found')
        found = True
        break
else:
    print("not found")
