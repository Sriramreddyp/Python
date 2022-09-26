numbers = [1, 2, 3]

print(*numbers)  # Unpacking operator

values = list(range(5))
Values_unpack = [*range(5), *"Hello"]
print(values)


first = {"x": 1}
second = {"x": 2, "y": 4}

combined = {**first, **second}

print(combined)
