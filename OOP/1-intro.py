# Object-oriented programming
# Not specific to Python, but Python is an OOP language
# Interaction objects within a program

x = 1

# x is an object of type int

y = "some text"

# y is an object of type str

z = [1, 2, 3]

# z is an object of type list

# x, y, z are variables that store the reference to the object of specific type

# we create instances of classes

# class is a blueprint for creating objects

print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>
print(type(z)) # <class 'list'>

# Class is something that built in Python that defines the behavior of an object (interactions with other objects in the program)
# Exaple:
# x + y # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Methods
# Methods are functions that are defined inside the body of a class

# Example:
z.append(4) # append is a method of the list class
print(z) # [1, 2, 3, 4]

y.append("a") # AttributeError: 'str' object has no attribute 'append'

# Almost everything in Python is an object
def func():
    print("Hello")

print(type(func)) # <class 'function'>

# Instances
# Instances are specific objects that are created from a particular class
x = 1 # x is an instance of the int class
y = "some text" # y is an instance of the str class

# Classes
# Classes are used to create new user-defined data structures that contain arbitrary information about something