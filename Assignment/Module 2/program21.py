# Write a Python program to convert two lists into one dictionary using a for loop

keys=["name","age","course"]
values=["Parth","20","python"]

student={}

for i in range (len(keys)):
    student[keys[i]]=values[i]

print("Dictionary:",student)

