import re
phone = "9876543210"
pattern=re.fullmatch(r"^[6-9]\d{9}",phone)
if pattern:
    print("Valid")
else:
    print("Not Valid")