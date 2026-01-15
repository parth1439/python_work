# 6) Write a Python program to check the current position of the file cursor using tell().

file=open("sample.txt",'w+')
file.write("hello! python")

position=file.tell()
print("Current file cursor position:", position)
file.close()

