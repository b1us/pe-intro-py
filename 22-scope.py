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