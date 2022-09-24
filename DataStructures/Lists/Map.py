items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = []
# for item in items:
#     prices.append(item[1])


prices = list(map(lambda item: item[1], items))  # Returns Map object

# for item in x:
#     prices.append(item)


print(prices)
