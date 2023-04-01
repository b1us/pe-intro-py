# Methods
#
# Methods are functions that are defined inside the body of a class. 
# They are used to define the behaviors of an object.

# Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self): # create a function inside the class = method # self is required as the first argument
        print("Hello, my name is", self.name) # self.name is the name attribute of the object instance

person1 = Person("John", 30)
person1.say_hello() # Hello, my name is John

# Add new methods to the class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name)

    def say_age(self):
        print("I am", self.age, "years old")

person1 = Person("Jhahahaha", 20)
person1.say_hello() # Hello, my name is John
person1.say_age() # I am 20 years old
