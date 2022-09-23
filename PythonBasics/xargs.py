def multiply(a, b):
    return a * b


def multiply_args(*list):
    total = 1
    for number in list:
        total += number
    return total


multiply_args(2, 3, 4, 5)
