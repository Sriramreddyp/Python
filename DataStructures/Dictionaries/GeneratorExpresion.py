from sys import getsizeof


values = (x for x in range(1000000000000))
print(type(values))  # Generator
print(getsizeof(values))
