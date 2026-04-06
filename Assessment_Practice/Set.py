
# Given a list:
# data = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7]

# Using one line of code:
# Create a set of squares of only odd numbers

# The square must be greater than 10

# Expected output:
# {25, 49}

data = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7]
result={x**2 for x in data if x % 2!=0 and x**2>10}
print(result)