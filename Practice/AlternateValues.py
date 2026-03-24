# 1)Alternate Values from Multiple Lists (Round Robin)
# Write a function that takes two lists and returns a new list by alternating elements from each list.
# If one list is longer than the other, append the remaining elements at the end.
# Example:
# a = [1, 2]
# b = ['a', 'b', 'c']

# # Expected:
# # [1, 'a', 2, 'b', 'c']

a = [1, 2]
b = ['a', 'b', 'c']
c=[]
for i in range(0,min(len(a),len(b))):
    c.append(a[i])
    c.append(b[i])
c.extend(a[i+1:])
c.extend(b[i+1:])
print(c)