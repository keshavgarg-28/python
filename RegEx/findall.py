import re
text="my phone number is 9876543210 and 1234567890"
result=re.findall(r"\d+", text)
print(result)

text="a1b22c333"
result=re.findall(r"\d+",text)
print(result)

text = "Hello 123 world Python"
result=re.findall(r"[a-zA-Z]+",text)
print(result)