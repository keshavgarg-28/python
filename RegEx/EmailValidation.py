import re
email = "test.email123@gmail.com"
pattern=re.fullmatch(r"^[a-zA-Z0-9.%+-]+@[a-zA-z0-9]+\.[a-zA-Z]+$",email)
if pattern:
    print("Valid Email")
else:
    print("Not Valid")
  