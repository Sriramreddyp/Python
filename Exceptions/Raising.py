from timeit import timeit


code1 = """

def calculate_xFactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")  # Same as throw
        return 10 / age

# Correct method to rasing exceptions


try:
    calculate_xFactor(-1)
except ValueError as error:
    # print(error)
    pass 

"""


code2 = """

def calculate_xFactor(age):
    if age <= 0:
       return None
       # Same as throw
       return 10 / age

# Correct method to rasing exceptions

xFactor = calculate_xFactor(-1)
if xFactor == None:
   pass
  

"""


print("First Code", timeit(code1, number=10000))
print("Second Code", timeit(code2, number=10000))
