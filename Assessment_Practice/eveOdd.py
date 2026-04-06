# Question 1 – Loops, Conditionals, List, Dictionary
# You are given a list of numbers:
# nums = [10, 15, 20, 25, 30, 35, 40]
# Write a function that:
# Iterates over the list
# Creates a dictionary where:
# keys are the numbers
# values are
# "Even" if the number is even
# "Odd" if the number is odd
# But skip numbers divisible by both 3 and 5
# # 

nums = [10, 15, 20, 25, 30, 35, 40]
d={}
for i in nums:
    if i%3==0 and i%5==0:
        continue
    if i%2==0:
        d[i]= "Even"
    elif i%2!=0:
        d[i]="Odd"
print(d)