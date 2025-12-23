# Write a Python program to separate keys and values from a dictionary using keys() and values() methods.

student={
    "name":"parth",
    "age":"20",
    "email":"parth@gmail"
}
keys=student.keys()
Values=student.values()

print("keys:",list(keys))
print("values:",list(Values))