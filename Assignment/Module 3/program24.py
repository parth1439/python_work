import re

text="python is programming language"
word="python"

result=re.match(word,text)

if result:
    print("word match")
else:
    print("word not match")