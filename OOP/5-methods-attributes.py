# Class Methods and Attributes

# Class Methods and Class Attributes differ from Instance Methods and Instance Attributes
# It's act in the class level, not in the instance level

class Car:
    def __init__(self, make, model): # instance method
        self.make = make # instance attribute
        self.model = model # instance attribute

class Car1:
    wheels = 4 # class attribute

    def __init__(self, make, model): # instance method
        self.make = make # instance attribute
        self.model = model # instance attribute

# print(Car.wheels) # AttributeError: type object 'Car' has no attribute 'wheels'
print(Car1.wheels) # 4

Car1.wheels = 12
print(Car1.wheels) # 12

# access class attributes using class name or instance name
c1 = Car1('BMW', 'X5')
c2 = Car1('Audi', 'A6')
print(c1.wheels) # 12
print(c2.wheels) # 12
print(Car1.wheels) # 12