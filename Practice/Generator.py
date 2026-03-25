# Question 4: Reverse List Using Generator
# Problem Statement:
# Write a generator function that yields elements of a list in reverse order.
# Example 1:
# Input: [1, 2, 3, 4]
# Output: 4 3 2 1
# Example 2:
# Input: [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;]
# Output: c b a

def my_gen(lst):
    for i in range(len(lst)-1,-1,-1):
        yield lst[i]
for i in my_gen([1,2,3,4]):
    print(i,end=" ")