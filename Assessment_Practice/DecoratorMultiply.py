# Task 2:
# Create a Python decorator called execution_logger that performs the following:
# Displays a message before a function runs:
#  Starting execution of <function_name>
# Displays a message after the function completes:
#  Completed execution of <function_name>
# Define a function multiply_numbers(x, y) that:
# Takes two numbers as arguments
# Returns their multiplication result
# Apply the execution_logger decorator to the multiply_numbers function.

def execution_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Starting execution of {func.__name__}")
        print(func(*args, **kwargs))
        print(f"Completed execution of {func.__name__}")
        return func
    return wrapper
    
@execution_logger
def multiply_numbers(x,y):
    return x*y
multiply_numbers(4,5)


# def execution_logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Starting execution of {func.__name__}")
#         print(func(*args, **kwargs))
#         print(f"Completed execution of {func.__name__}")
#         return func
#     return wrapper


# @execution_logger
# def multiply_numbers(x,y):
#     return x*y
# multiply_numbers(3,4)