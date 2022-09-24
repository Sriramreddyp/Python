items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

x = filter(lambda item: item[1] >= 10, items)

# lambda can only return single type
# if returns boolean
# normal return returns whatever we return

for item in x:
    print(item)
