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

# Return values from functions:
# Example5 (return a value):
def add_10(x, y):
    result = x + y + 10
    return result # as soon as we hit the return statement, the function stops executing
    print("hi") # this line will never be executed 

result = add_10(10, 20) # we can assign the return value to a variable
print(result)

# Example6 (multiple return values):
def add_sub(x, y):
    add = x + y
    sub = x - y
    return add, sub # we can return multiple values

add, sub = add_sub(10, 20) # we can assign the return values to multiple variables
print(add)
print(sub)

# Optional parameters and default values:
# Example7 (optional parameters):
def add_5(x, y, z=0): # z is an optional parameter
    result = x + y + z + 5
    print(result)

add_5(10, 20) # z is optional, so we can call the function without passing a value for z
add_5(10, 20, 30) # z is optional, so we can call the function and pass a value for z

# range() is a built-in function that returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. So it looks like this: range(start, stop, step)

def new_range(start = 0, stop = 10, step = 1): # default values are set
    i = start
    while i < stop:
        print(i)
        i += step

new_range() # default values will be used
new_range(5) # start will be 5, stop will be 10, step will be 1
new_range(5, 20) # start will be 5, stop will be 20, step will be 1
new_range(5, 20, 2) # start will be 5, stop will be 20, step will be 2

# Positionaly
# arguments are passed to the function in the same order as the parameters are defined
# but we can also pass arguments by keyword / named arguments
new_range(step=3) # start will be 0, stop will be 10, step will be 3
new_range(start=-5) # start will be -5, stop will be 10, step will be 1

# parameter that doesn't have a default value must be passed before parameters that have default values
# new_range(step=3, 5) # this will give an error
# new_range(5, step=3) # this will work (important). Python rules: positional arguments must come before keyword arguments

# Return multiple values from a function:
def return_values(x, y):
    return x + 1, y + 1

result = return_values(10, 20)
print(result) # this will print a tuple
a, b = return_values(10, 20)
print(a) # this will print 11
print(b) # this will print 21
print(a, b) # this will print 11 21

# Example8 (remove characters from a string)
def remove_chars(base, chars):
    new_string = base
    for char in chars:
        new_string = new_string.replace(char, "")
    return new_string

print(remove_chars("hello world", "l")) # this will print heo word

# Example9 (sum of all numbers in a list)
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4, 5])) # this will print 15

# Example10 (sum of all numbers in each lists)
def sum_each_lists(lst1, lst2):
    sum_list1 = sum_list(lst1)
    sum_list2 = sum_list(lst2)
    return sum_list1, sum_list2

print(sum_each_lists([1, 2, 3], [4, 5, 6])) # this will print (6, 15)

# Example11 (sum of all numbers in all lists)
def sum_all_lists(*lists): # *lists is a tuple
    total = 0
    for lst in lists:
        total += sum_list(lst)
    return total

print(sum_all_lists([1, 2, 3], [4, 5, 6], [7, 8, 9])) # this will print 45