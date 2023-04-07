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
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name)

    def say_age(self):
        print("I am", self.age, "years old")

person1 = Person1("Jhahahaha", 20)
person1.say_hello() # Hello, my name is John
person1.say_age() # I am 20 years old

# Setters and Getters (accessors and mutators) methods
class Person2:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
    
person1 = Person2("Johny")
person1.set_age(20)
print(person1.get_age()) # 20
# get is redundant, we can use the attribute directly
print(person1.age) # 20
# So this is a bad example, but it's just to show you how it works
# This is not a good practice

# Example: create a class called Student
class Student1:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
    
student1 = Student1("Johno")
student1.say_hello() # Hello, my name is Johny
# student1.get_age() # AttributeError: 'Student' object has no attribute 'age' 
# because we haven't set the age yet

# So we need to set the age first
# We can do this by using the set_age method
# student1.set_age(20)
# or we can do this by using the attribute directly
# student1.age = 20
# or we can do this by using the __init__ method
# student1 = Student("Johny", 20)
# or we set default value for the age attribute
class Student2:
    def __init__(self, name):
        self.name = name
        self.age = None # default value so we don't get an error when we call the get_age method before setting the age # this is if we want to use this attribute later on

    def say_hello(self):
        print("Hello, my name is", self.name)

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
    
student1 = Student2("Johne")
student1.say_hello() # Hello, my name is Johny
student1.get_age() # None
print(student1.age) # None
student1.set_age(20)
print(student1.age) # 20

# Example: create a class called Counter
# This class will keep track of the number of times in increase or decrease state
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
    
    def decrement(self):
        self.count -= 1

    def print_count(self):
        print(f"The current count is {self.count}")

counter1 = Counter()
counter1.print_count() # The current count is 0
counter1.increment()
counter1.print_count() # The current count is 1
counter1.increment()
counter1.print_count() # The current count is 2
counter1.decrement()
counter1.print_count() # The current count is 1