# Question 5: Recursive Digit Sum
# Problem Statement:
# Write a recursive function that calculates the sum of digits of a number.
# Example 1:
# Input: 1234
# Output: 10
# Example 2:
# Input: 507
# Output: 12
# Example 3:
# Input: 9
# Output: 9"

def digitsum(n):
    if n==0:
        return 0
    dig=n%10
    return dig+digitsum(n//10)

print(digitsum(9))