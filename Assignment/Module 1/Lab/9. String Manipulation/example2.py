s = "  Python Programming Language  "

print("Original String:", s)

# String methods
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title Case:", s.title())
print("Capitalized:", s.capitalize())

print("Stripped String:", s.strip())
print("Left Strip:", s.lstrip())
print("Right Strip:", s.rstrip())

print("Replace word:", s.replace("Python", "Java"))
print("Find 'Program':", s.find("Program"))
print("Count 'a':", s.count('a'))

print("Starts with 'Python':", s.strip().startswith("Python"))
print("Ends with 'Language':", s.strip().endswith("Language"))

print("Split into words:", s.split())
