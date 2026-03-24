# Task 2:
# Given a list of numbers (as strings):
# nums = ["10", "20", "abc", "30", "5"]
# Tasks
# Convert valid numbers to integers (ignore invalid values using exception handling).
# 1.keep only numbers greater than 10.
# 2.square the remaining numbers.
# 3.find the sum of squared values.
from functools import reduce
nums = ["10", "20", "abc", "30", "5"]
valid=[]
for x in nums:
    try:
        num=int(x)
        valid.append(num)
    except:
        pass
print(valid)
filtered=list(filter(lambda x:x>10,valid))
print(filtered)
squared=list(map(lambda x: x**2, filtered))
print(squared)
sum=reduce(lambda a,b:a+b, squared)
print(sum)