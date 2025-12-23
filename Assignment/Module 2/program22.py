# Write a Python program to count how many times each character appears in a string.

text="python"
char_count={}

for ch in text:
    if ch in char_count:
        char_count[ch]+=1
    else:
        char_count[ch]=1

print("character count")
print(char_count)

