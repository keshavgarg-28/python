# Question 5 – Generators, Regex
# Write a generator function that:
# Takes a list of strings
# Yields only strings that are valid email IDs

# Conditions for valid email:
# Must contain @
# Must end with .com
# Example input:
# emails = ["test@gmail.com", "hello@abc", "user@yahoo.com", "admin@site.org"]

# Expected output when iterated:
# test@gmail.com
# user@yahoo.com
import re
emails = ["test@gmail.com", "hello@abc", "user@yahoo.com", "admin@site.org"]

def my_gen(emails):
    for i in emails:
        pattern=re.fullmatch(r"([a-zA-Z]+@[a-zA-Z]+\.com)", i)
        if pattern:
            yield i
for i in my_gen(emails):
    print(i)