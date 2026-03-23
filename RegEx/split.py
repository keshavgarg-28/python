import re
text = "apple, banana, mango orange"
result =re.split(r"[, ]+",text)
print(result)


text = "one1two2three3"
result = re.split(r"\d", text)
print(result)