import re
text="a1b22c333"
for i in re.finditer(r"\d+",text):
    print(i.group(),i.start(),i.end())