# Task 5
# Write a Python program to validate email addresses using regex.
# Valid format: username@domain.extension
# Username: alphanumeric and underscores
# Domain: alphanumeric
# Extension: 2-4 letters
# Test cases:
# python
# emails = [""user@example.com"", ""invalid.email"", ""test_123@domain.co.uk"", ""@nodomain.com""]"


import re
emails = ["user@example.com", "invalid.email", "test_123@domain.co.uk", "@nodomain.com"]
for i in emails:
    pattern = re.fullmatch(r"^([a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$)", i)
    if pattern:
        print("VALID")
    else:
        print("NOT VALID")