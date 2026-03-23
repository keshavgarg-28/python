import re
texts = ["abc123", "xyz456", "no number"]
pattern=re.compile(r"\d+")
for i in texts:
    result=pattern.findall(i)
    print(result)

texts = ["123abc", "456def", "789ghi"]
pattern=re.compile(r"[a-z]+")
for i in texts:
    result=pattern.search(i)
    if result:
        print(result.group())