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

# Attributes
# Attributes are pieces of information that are associated with a class or an object
# Attributes can be accessed using the dot notation
# Example:
class PersonNew:
    def __init__(self, name):
        self.name = name # name is an attribute of the class PersonNew
        # self is a reference to the object itself

person4 = PersonNew("Doe") # self is referring to the object person4
person5 = PersonNew("Smith") # self is referring to the object person5
print(person4.name) # Doe
print(person5.name) # Smith
print(person3.name) # Jane

# Modifying attributes from outside the class

person4.some_attribute = "some value"
print(person4.some_attribute) # some value

person4.name = "Name changed"
print(person4.name) # Name changed

# Example:
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

a = Fruit("Apple", 100)
b = Fruit("Banana", 200)
a.color = "Red"
print(a.name, a.calories, a.color) # Apple 100 Red
print(b.name, b.calories) # Banana 200

# Purpose of the Class
# Classes are used to create new user-defined data structures that contain arbitrary information about something
