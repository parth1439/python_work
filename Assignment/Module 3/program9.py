# Write a Python program to handle file exceptions and use the finally block for closing the file. 

try:
    file=open("sample.txt",'r')
    content=file.read()
    print("file content")
    print(content)

except FileNotFoundError:
    print("error file not found")

finally:
    if 'file' in locals():
        file.close()
        print("file closed")