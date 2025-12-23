#  Practical Example 2: Write a Python program to find the length of each string in List1.

list1 = ['apple', 'banana', 'mango']
for fruits in list1:
    count=0
    for ch in fruits:
        count+=1
    print(fruits," : ",count)

