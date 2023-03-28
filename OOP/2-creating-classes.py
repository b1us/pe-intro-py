# Creating Classes

# Classes are used to create new user-defined data structures that contain arbitrary information about something

# Classes are created by keyword `class`
# Class names should be written in `PascalCase` not `camelCase`

# Example:
class PersonInTheMoon:
    pass

# Instantiating a class
# Creating an instance of a class is called instantiation
# We can instantiate a class by calling it like a function
# Example:
person = PersonInTheMoon() # This is an instance of the class PersonInTheMoon
print(person) # <__main__.PersonInTheMoon object at 0x7f9b9c0b7a90> 
# This is the memory address of the object 
# The __main__ part is the name of the module in which the class was defined (in this case, the file which we are running)
print(type(person)) # <class '__main__.PersonInTheMoon'>
# This is the type of the object

# The __init__ method
# Known as dunder (double underscore) method or magic method or constructor method or initializer method 
# The __init__ method is a special method which is called when an object is instantiated

# Example:
class Person:
    def __init__(self):
        print("Person1 instantiated")

person1 = Person() # Person instantiated
print(person1) # <__main__.Person object at 0x7f9b9c0b7a90>
print(type(person1)) # <class '__main__.Person'>

# The __init__ method can take arguments
# Required arguments must be passed when instantiating the class
# Example:
class Person:
    def __init__(self, name, age):
        print("Person2 instantiated")
        self.name = name
        self.age = age

person2 = Person("John", 30) # Person2 instantiated
print(person2.name) # John
print(person2.age) # 30

person3 = Person("Jane", 25) # Person3 instantiated
print(person3.name) # Jane
print(person3.age) # 25
