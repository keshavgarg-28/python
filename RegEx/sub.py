import re
text = "My marks are 90 and 85"
result=re.sub(r"\d+", "xx",text)
print(result)


text = "Hello World Python"
result = re.sub(r"\s+", "", text)
print(result)