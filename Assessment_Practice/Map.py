# "Question 1: Square Numbers Using map()
# Problem Statement:
# Write a function that takes a list of numbers and returns a new list containing the square of
# each number using map().
# Example 1:
# Input: [1, 2, 3, 4]
# Output: [1, 4, 9, 16]
# Example 2:
# Input: [5, 6]
# Output: [25, 36]
# Example 3:
# Input: []
# Output: []

lst=[1,2,3,4]
mapped=list(map(lambda x: x**2, lst))
print(mapped)
