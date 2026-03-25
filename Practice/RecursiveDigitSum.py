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

def digit_sum(n,sum):
    if(n==0):
        return 0
    dig=n%10
    return dig+digit_sum(n//10,sum)
print(digit_sum(1234,0))
print(digit_sum(507,0))
print(digit_sum(9,0))