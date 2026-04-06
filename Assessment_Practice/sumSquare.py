# Task 2:
# Given a list of numbers (as strings):
# nums = [""10"", ""20"", ""abc"", ""30"", ""5""]
# Tasks
# Convert valid numbers to integers (ignore invalid values using exception handling).
# 1.keep only numbers greater than 10.
# 2.square the remaining numbers.
# 3.find the sum of squared values.
from functools import reduce
nums = ["10", "20", "abc", "30", "5"]
valid=[]
for i in nums:
    try:
        num=int(i)
        valid.append(num)           
    except:
        pass

print(valid)
filtered=list(filter(lambda x:x>10,valid))
print(filtered)
mapped=list(map(lambda x: x**2, filtered))
print(mapped)
reduced=reduce(lambda x,y:x+y, mapped)
print(reduced)