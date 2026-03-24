# 3)Invert a Dictionary
# Write a function that inverts a dictionary.
# Keys should become values.
# Values should become keys.
# Assume all values in the original dictionary are unique.
# Example:
# d = {"a": 1, "b": 2, "c": 3}

# # Expected:
# # {1: "a", 2: "b", 3: "c"}

d = {"a": 1, "b": 2, "c": 3}
res={}
for k,v in d.items():
    res[v]=k
print(res)