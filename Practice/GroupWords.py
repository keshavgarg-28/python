# 2)Group Words by Length
# Write a function that groups a list of words based on their length.
# The function should return a dictionary where:
# Keys represent word lengths.
# Values are lists of words having that length.
# Example:
# words = ["cat", "dog", "elephant", "bat", "ant"]

# # Expected:
# # {
# #   3: ["cat", "dog", "bat", "ant"],
# #   8: ["elephant"]
# # }

words = ["cat", "dog", "elephant", "bat", "ant"]
dict={}
for i in words:
    length=len(i)
    if length not in dict:
        dict[length]=[]
    dict[length].append(i) 
print(dict)
