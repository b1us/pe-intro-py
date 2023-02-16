# Functions
#
# A reuseable block of code that performs a specific task and can be called upon to do something at a later time multiple times.
# Some functions take some arguments and some don't.
# Some functions return a value and some don't.
# Some functions are built into Python and some are not.
# Example of a built-in function:
# print(), input(), len(), type(), int(), float(), str(), etc.
# Here we're focus on creating our own functions.
# 
# Syntax:
# def function_name():
#     # code
#
# Example1 (no parameters to accept arguments):
def say_hello1():
    print("Hello!")

# Example2 (takes a parameter to accept an argument):
def say_hello2(name): # "name" is the parameter
    print(f"Hello {name}!")

# To call a function:
say_hello1()
say_hello2("John") # "John" is the argument
say_hello1()
say_hello2("Jane") # "Jane" is the argument

# Example3 (takes multiple parameters to accept multiple arguments): you can have as many parameters as you want
def add_5(x, y):
    result = x + y + 5
    print(result)

add_5(10, 20)

# Example4 (we could takes variables as arguments):
def add_100(a, b, c):
    result = a + b + c + 5
    print(result)

num1 = 10
num2 = 20
num3 = 30
add_100(num1, num2, num3)
add_100(num1, num1, num1)
