try:
    age = int(input("Age "))
except ValueError as ex:
    print("You Didnt entered a valid age")
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print("You Didnt entered a valid age")
else:
    print("Execution Continues...... ")

print("Execution Continues ....")
# Value Error Exceptions


# Double exception

try:
    age = int(input("Age "))
except (ValueError, ZeroDivisionError):
    print("You Didnt entered a valid age")


# try:
#     file = open("Exceptions.py")


# finally:
#     file.close()


# context management protocol - with statement - enter and exit method

# With statement
try:
    # used to automatically release external resources
    with open("Execution.py") as file:
        print('file Opened')

    age = int(input("Age "))
except (ValueError, ZeroDivisionError):
    print("You Didnt entered a valid age")
