# Scope
# 

# Global scope
x = 1

def f():
    # Local scope
    y = 2
    print(y) # 2
    print(x) # 1 # global scope is accessible from local scope

f()
print(x) # 1
# print(y) # NameError: name 'y' is not defined # local scope is not accessible from global scope => block scope => scope is defined by indentation (not by {}) => can look outside the scope but not inside

# Block scope
inp = int(input('Enter a number: '))

if inp > 5:
    value = "Greater than 5" # if the value in not greater than 5 (for example 3), the variable is not defined => NameError: name 'value' is not defined
else:
    value = "Less than 5"
    # if the value already defined, it will be accessible outside the block

print(value) 

# block scope example from inside the function
def f():
    if inp2 > 5:
        value = "Greater than 5: inside the function"
    else:
        value = "Less than 5: inside the function"
    print(value) # the variable is defined inside the block => it is accessible inside the function

inp2 = int(input('Enter a number: '))
f()
print(f"from outside the function: {value}")

# More examples
def add_5(b):
    b = b + 5 # b is a local variable
    print(f"inside", b) # 15 

b = 10 # b is a global variable
print(f"outside", b) # 10 
add_5(b)
print(f"outside", b) # 10

# example with list
def append_5(lst):
    lst.append(5) # lst is a local variable
    print(f"inside", lst) # [5]

lst = [] # lst is a global variable
print(f"outside", lst) # []
append_5(lst)
print(f"outside", lst) # [5]

# Global keyword
#
# if we want to change the global variable inside the function, we need to use the global keyword
# considered as a bad practice
# avoid using it at all costs
# if we use it, we should use it only once in the function
# this is just an example for educational purposes, we should not use it in real life

value = 5

def foo():
    global value
    value = 10 # we are changing the global variable value of 5 to 10 inside the function every time we call the function

print(value) # 5
foo()
print(value) # 10

value = 20
foo()
print(value) # 10 => the global variable is changed inside the foo() function 