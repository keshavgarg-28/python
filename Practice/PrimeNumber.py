# Task 3:
# Write a Python program to print all prime numbers up to a given number N.
# Requirements
# Take an integer input N

# Print all prime numbers from 2 to N (inclusive)

n=int(input("Enter a number: "))

for i in range(2, n+1):
    c=0
    for j in range(2,i):
        if(i%j==0):
            c=c+1
            break
    if(c==0):
        print(i)