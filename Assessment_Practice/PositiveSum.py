
# Question 2: Sum of Positive Numbers Using reduce()
# Problem Statement:
# Write a function that uses reduce() to calculate the sum of only positive numbers in a list.
# Example 1:
# Input: [1, -2, 3, -4, 5]
# Output: 9
# Example 2:
# Input: [-1, -5, -10]
# Output: 0
# Example 3:
# Input: [10, 20, 30]
# Output: 60

from functools import reduce
lst=[1,-2,3,-4,5]
filtered=list(filter(lambda x: x>0, lst))
reduced=reduce(lambda x, y: x+y, filtered)
print(reduced)