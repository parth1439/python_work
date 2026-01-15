# 10) Write a Python program to print custom exceptions.


class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise AgeError("Age must be 18 or above")
    else:
        print("Access granted")

except AgeError as e:
    print("Custom Exception Occurred:")
    print(e)

except ValueError:
    print("Invalid input! Please enter a number.")
