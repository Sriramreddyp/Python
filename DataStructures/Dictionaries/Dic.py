# Dictionary = key,value  pairs

point = {"x": 1, "y": 2}

point_dict = dict(x=1, y=2)

print(point["x"])

for x in point:
    print(point.get(x))

del point["x"]

for key, value in point.items():
    print(key, value)
