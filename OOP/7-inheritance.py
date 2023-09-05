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

# Method overloading example 2
class Employee3(Person):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name) # call the parent class constructor is mandatory
        self.salary = salary

    def say_hello(self):
        super().say_hello()
        print(f"My salary is {self.salary}")
        
e3 = Employee3("Alice", "Wonderful", 10000)
e3.say_hello() # Hello, my name is Alice Wonderful
# e3.test() # AttributeError: 'Employee3' object has no attribute 'test'

class Manager(Employee3):
    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, last_name, salary)
        self.department = department

    def say_hello(self):
        super().say_hello()
        print(f"I am a manager in {self.department} department and my salary is {self.salary}")

m1 = Manager("Bob", "Marley", 20000, "IT")
m1.say_hello() # Hello, my name is Bob Marley

class Owner(Person):
    def __init__(self, first_name, last_name, company):
        super().__init__(first_name, last_name)
        self.company = company

    def say_hello(self):
        super().say_hello()
        print(f"I am the owner of {self.company}")

o1 = Owner("John", "Doe", "ABC")
o1.say_hello() # Hello, my name is John Doe

# Check if an object is an instance of a class
print(isinstance(o1, Owner)) # True
print(isinstance(o1, Person)) # True
print(isinstance(o1, Employee1)) # False
print(isinstance(o1, Employee2)) # False
print(isinstance(o1, Employee3)) # False
print(isinstance(o1, Manager)) # False


# Multiple inheritance
class A:
    def __init__(self):
        print("A init")

class B:
    def __init__(self):
        print("B init")

class C(A, B):
    pass

c = C() # A init

class D(B, A):
    pass

d = D() # B init

class E:
    pass

class F(E, A):
    pass

f = F() # A init

class G:
    def __init__(self):
        print("G init")

class H:
    def __init__(self):
        print("H init")

class I(G, H):
    def __init__(self):
        super().__init__()
        print("I init")

        # Method Resolution Order (MRO) determines the order of method lookup for classes involved in multiple inheritance.

i = I() # G init

# Duck typing

class Duck:
    def swim(self):
        print("Duck can swim")

    def fly(self):
        print("Duck can fly")

class Whale:
    def swim(self):
        print("Whale can swim")

animals = [Duck(), Duck(), Whale()]

for animal in animals:
    animal.swim() # Duck can swim, Whale can swim
    # animal.fly() # AttributeError: 'Whale' object has no attribute 'fly'
    # Duck typing allows us to treat objects differently based on the methods they support, rather than their type. Here we can call swim on both Duck and Whale objects even though they are of different types. This is because both of them support the swim method. However, we cannot call fly on Whale object because it does not support the fly method.