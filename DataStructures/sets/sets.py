numbers = [1, 1, 2, 2, 3, 3, 4, 4]
first = set(numbers)
second = {1, 5}
# second.add(5)
# len(second)
# print(uniques)s

print(first | second)  # union
print(first & second)  # intersection
print(first - second)  # difference
print(first ^ second)


# print(first[0]) #doesnt support indexing

if 1 in first:
    print("yes")
