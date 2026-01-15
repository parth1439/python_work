import re

text="python is programming language"
word="language"

find=re.search(word,text)

if find:
    print("word find")
else:
    print("word not find")
