# 7) Write a Python program to handle exceptions in a calculator
try:
    
    a=int(input("enter a number"))
    b=int(input("enter a number"))

    print("addition :",a+b)
    print("subtraion :",a-b)
    print("multiplication :",a*b)
    print("division :",a/b)

except ZeroDivisionError:
    print("error can not division by zero")

except ValueError:
    print("error please enter a valid intigers")

finally:
    print("end program")