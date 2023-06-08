# Inheritance

# Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes (ancestors).

# Polymorphism

# Polymorphism is the concept by which we can define methods in the child class with the same name as defined in their parent class. This helps us in defining a method in the child class that can perform a specific action depending on the child class instance.

# Supercalss / base class / parent class
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name  = last_name

    def say_hello(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}")

# Inheritance / child class / derived class / subclass
class Employee1(Person):
    def test(self):
        print("test")

e = Employee1("John", "Doe")
e.say_hello() # Hello, my name is John Doe

p = Person("Jane", "Doll")
p.say_hello() # Hello, my name is Jane Doll
# p.test() # AttributeError: 'Person' object has no attribute 'test'

# Overriding methods in child class using super()
class Employee2(Person):
    def say_hello_employee(self):
        print("---say hello from child class---")
        super().say_hello()
        print("--------------------------------")

e2 = Employee2("Jordan", "Donkey")
e2.say_hello_employee() 