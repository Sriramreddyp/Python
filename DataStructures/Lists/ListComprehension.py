items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filtered = filter(lambda item: item[1] >= 10, items)
# filtered = [item for item in items if item[1] >= 10]


prices = [item[1] for item in items]
prices = list(map(lambda item: item[1], items))
