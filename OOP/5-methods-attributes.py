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

# instance attributes override class attributes
class Car2:
    wheels = 4 # class attribute

    def __init__(self, make, model): # instance method
        self.make = make # instance attribute
        self.model = model # instance attribute
        self.wheels = 5 # instance attribute

c3 = Car2('BMW', 'X5')
c4 = Car2('Audi', 'A6')
print(c3.wheels) # 5
print(c4.wheels) # 5
print(Car2.wheels) # 4

# modify class attributes using instance attributes
class Car3:
    number_of_car = 0 # class attribute

    def __init__(self, make, model): # instance method
        self.make = make # instance attribute
        self.model = model # instance attribute
        Car3.number_of_car += 1 # class attribute

c5 = Car3('BMW', 'X5')
c6 = Car3('Audi', 'A6')
c7 = Car3('Toyota', 'Camry')
print(c5.number_of_car) # 3
print(c6.number_of_car) # 3
print(c7.number_of_car) # 3


# Class Methods
# Class methods are methods that are bound to the class and not the object of the class (instance)

class Car4:
    number_of_car = 0 # class attribute

    def __init__(self, make, model): # instance method
        self.make = make # instance attribute
        self.model = model # instance attribute
        Car4.number_of_car += 1 # class attribute

    @classmethod # can only access class attributes, not instance attributes
    def get_number_of_car(cls): # cls is the class itself
        return cls.number_of_car
    
c8 = Car4('BMW', 'X5')
c9 = Car4('Audi', 'A6')
c10 = Car4('Toyota', 'Camry')
print(Car4.get_number_of_car()) # 3
print(c8.get_number_of_car()) # 3
print(c9.get_number_of_car()) # 3
print(c10.get_number_of_car()) # 3

# Class Methods and Attributes

class Circle:
    pi = 3.14 # class attribute

    @classmethod # can only access class attributes, not instance attributes
    def area(cls, radius): 
        return cls.pi * (radius ** 2)
    
    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius
    
    @classmethod
    def get_area_and_perimeter(cls, radius):
        return cls.area(radius), cls.perimeter(radius)
    
print(Circle.area(5)) # 78.5
print(Circle.perimeter(5)) # 31.400000000000002
print(Circle.get_area_and_perimeter(5)) # (78.5, 31.400000000000002)

# Class methods and attributes can only access class attributes, not instance attributes