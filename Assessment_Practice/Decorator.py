# Question 3: Count Function Calls Using Decorator
# Problem Statement:
# Write a decorator that counts how many times a function is called and prints the count.
# Example 1:
# Call function 3 times
# Output:

# Function called: 3 times
# Example 2:
# Call function 1 time
# Output:
# Function called: 1 time

def count(func):
    c=0
    def wrapper():
        nonlocal c
        c+=1
        print(f"Function executed {c} times.")
        return func
    return wrapper
@count
def Hello():
    print("hello")

Hello()
Hello()






















# def count(func):
#     c=0
#     def wrapper():
#         nonlocal c
#         c+=1
#         print(f"Function called {c} times")
#         return func()
#     return wrapper
# @count
# def main():
#     print("Hello")

# main()
# main()