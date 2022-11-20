# data types
# int = 0
# float = 1.0
# str = "Hello, string!"
# bool = False
# None

# print()
# msg = "Hello, world!"
# print(msg)
# print(int, float, str, bool, None)

# type()
# print(type(int))
# print(type(float))
# print(type(str))
# print(type(bool))
# print(type(None))

# print(type("something"))


# Single line comment

# ''' 
# Multi line comment 1
# '''

# """
# Multi line comment 2
# """

# print("inline comment") #  this is in line comment 

# print("take argument", "and", "print it on the screen", "\n this new line symbol makes it's printed in the new line", end=" and ended here, ")
# print("viola!")

# variable

# x = 3
# y = "hello"
# num = x

# print(x, y, num)

## naming variable -> 
# meaningful
# start with a letter (should be lowercase, because uppercase would be used in Class) or underscore. 
# number can be used after it but any other characters is invalid
# underscore to separate more than one (snake case is preferred, camel case is valid)
# case sensitive (start with )


# x = 5
# y = "AlgoExpert"
# z = True
# x = y
# y = z
# z = x
# print(z)

# hEllo = 1
# name_input_ = 2
# 1input = 3    invalid syntax
# h*llo = 4    invalid syntax
# _x = 5
# name input = 6    invalid
# y&s = 7    invalid syntax
# void* = 8    invalid syntax
# tim1 = 9
# hello.World = 10    invalid syntax

# string = "AlgoExpert is the best!"
# print(string)

# x = 2
# y = 7
# z = True

# print(x, y, z)

# console input
# input("Number: ")

# user_name = input("What is your username? ")
# print("Hello", user_name + "!")

# console input only accepts one argument, use `string concatenation`` if you need to include multiple arguments
# console output will always be str

# input("Press enter to begin!")

# name = input("Please anter your name: ")
# age = input("Hello, " + name + " what is your age: ")
# print("Hello,", name, "you are", age, "years old!")
# print("Hello, " + name + " you are " + age + " years old!")

# arithmetic operations. 
# works for different numbers types like floats and integers
# floats operations to integers = floats

# x = 2
# y = 3
# z = 4.5

# result = x + y
# result2 = x + z
# print(result)
# print(result2)

# operations
# substracton -
# multiply *
# division / the result will always be `floats`. Div by 0 will not work
# exponents **
# integer division // (rounds down)
# modulus %

# order operations (precedence)
# result = x % y + 4 - 7 ** (2 / 3) as follows
# brackets/parenthesis
# exponents
# multiplication and divisio and modulus
# additions and substractions

# operations on different data types 
# `integer` with `string`` = errors (TypeError)
# `int` with `True` = works => because True = 1; 
# `int` with `False`= error => because false = 0 => ZeroDivisionError

# type conversions
# example: string -> integer <-> float
x = "4"
y = int(x) + 4
z = float(x) + 4
a = str(0)
print(type(x))
print(type(y))
print(type(z))
print(type(a))

# bool -> empty string = false, otherwise = true,
# bool -> int 0 = false, otherwise = true,