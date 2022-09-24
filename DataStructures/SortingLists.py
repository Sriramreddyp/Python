numbers = [23, 354, 756, 23, 54, 1]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print(sorted(numbers))  # Returns new list

print(sorted(numbers, reverse=True))


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
