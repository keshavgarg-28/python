# 4)Merge Two Dictionaries
# Write a function that merges two dictionaries.
# If a key exists in both dictionaries, add their values.
# If a key exists in only one dictionary, keep its value unchanged.
# Example:
# d1 = {"a": 10, "b": 20}
# d2 = {"b": 5, "c": 15}
# # Expected Output:
# # {"a": 10, "b": 25, "c": 15}

d1 = {"a": 10, "b": 20}
d2 = {"b": 5, "c": 15}
for k,v in d2.items():
    if k not in d1:
        d1[k]=v
    else:
        d1[k]+=v
print(d1)
