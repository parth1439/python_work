fruits=["apple","banana","mango","orange"]
serach_item="mango"

for item in fruits:
    if item == serach_item:
        print(serach_item,"found this list")
        break
else:
        print(serach_item,"not found this list")