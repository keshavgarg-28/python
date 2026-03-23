import re
password = "Test1234"
pattern=re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}", password)
if pattern:
    print("Valid Password")
else:
    print("Invalid")