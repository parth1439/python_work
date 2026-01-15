# 8)Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

try:
    filename=input("enter file name:")
    file=open(filename,'r')
    print("file content:")
    print(file.read())

    a=int(input("enter a first number"))
    b=int(input("enter a second number"))
    print(file.read())

    file.close()

except FileNotFoundError:
    print("error file not found")

except ZeroDivisionError:
    print("error division by zero is not allowed")

except ValueError:
    print("error invalid input please enter numbers only")

except Exception as e:
    print("unexpected error",e)

else:
    print("program executed successfully")

finally:
    print("program finished")