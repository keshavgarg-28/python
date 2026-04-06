# Given a list of strings:
# words = ["Python", "java", "C", "javascript", "Go"]

# Using map, filter, and reduce:
# Filter words whose length is greater than 3

# Convert the filtered words to lowercase

# Find the total number of characters in the final list

# Do not use loops.
from functools import reduce
words = ["Python", "java", "C", "javascript", "Go"]
filtered= list(filter(lambda x: len(x)>3, words))
print(filtered)
mapped=list(map(lambda x:x.lower(), filtered))
print(mapped)
result=reduce(lambda x, y: x+y, map(len,mapped))
print(result)