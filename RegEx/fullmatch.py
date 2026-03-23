import re
text = "12345"
result=re.fullmatch(r"\d+",text)
if result:
    print("True")


username="python"
if re.fullmatch(r"[a-zA-z]{3,8}",username):
    print("Valid Username")
else:
    print("Invalid")