import re
text="abc123xyz456"
result=re.search(r"\d+",text)
print(result)
print(result.group())

text = "hello5world"
result=re.search(r"\d+",text)
print(bool(result.group()))