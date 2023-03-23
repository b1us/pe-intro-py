# Miscellaneous Python Syntax

# 1. Comprension
# is a way to create a list, dictionary or tuple in a single line of code

# 1.1 List comprension
lst = []
for i in range(1, 11):
    lst.append(i)

print(lst)

lst = [i for i in range(1, 11)] # put the for loop inside the list
print(lst)

lst = [i + 1 for i in range(1, 11)] # put the for loop inside the list
print(lst)

lst = [i * 2 for i in range(1, 11)] # put the for loop inside the list
print(lst)

lst = [i for i in range(1, 11) if i % 2 == 0] # put the if statement inside the list
print(lst)

lst = [i * j for i in range(1, 11) for j in range(5)] # put the for loop inside the list
print(lst)

# 1.2 Dictionary comprension

d = {i: i * 2 for i in range(1, 11)}
print(d) # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}

# 1.3 Set comprension

s = {i for i in range(1, 11)}
print(s) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 1.4 Tuple comprension (doesn't work) => (generator object) - advanced topic

# Multiple assignment
x = y = z = 10
print(x, y, z) # 10 10 10

# Unpacking 
# Unpacking a tuple into individual values (advanced topic)
x, y, z = 10, 20, 30 # or x, y, z = (10, 20, 30)
print(x, y, z) # 10 20 30

# Unpacking a list into individual values (advanced topic)
x, y, z = [10, 20, 30]
print(x, y, z) # 10 20 30

# Docstring (documentation string)
# is a string that is the first statement in a module, function, class, or method definition
# It is used to document the purpose of the function, class, method, etc.

def add(a, b):
    """
    This function adds two numbers
    """
    return a + b

print(add.__doc__) # This function adds two numbers

# Help function
# is a built-in function that displays the documentation string of a function, class, method, etc.

help(add) # Help on function add in module __main__:
            # add(a, b)
            #     This function adds two numbers

# Lambda function
# is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression

# 1.1 Lambda function with one argument
x = lambda a: a + 10
print(x(5)) # 15