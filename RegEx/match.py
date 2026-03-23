import re
text="123abc"
print(re.match(r"\d+",text).group())

text="Hello World"
result=re.match(r"Hello", text)
if result:
    print("String started with hello")