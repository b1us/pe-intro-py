# Abstract Class
# A class that never has any instances. 
# It should not be instantiated. 
# It's meant to be a parent class, superclass, or base class for other classes.
# It's objective is solely to increase the abstraction of the code.
# To contain the common implementation detalis (attributes and methods) of the classes that inherit from it.
# Methods: other than static, instance, and class methods, abstract class can have `abstract methods.

# Abstract Method
# An abstract method is a method that is declared in an abstract class but contains no implementation yet, but it is required to be implemented in the derived classes.

# Notes:
# Theoretically, Python does not have a keyword/notion to declare an abstract class.
# We can't actualy make something abstract. We can't force it to never be able to be instantiated.

# Abstract Class Example
class AbstractGame: # do not have to be named AbstractSomething, just for education purposes only.
    # Abstract method, as general as possible
    @staticmethod
    def start():
        while True:
            start = input("Would you like to start the game? (y/n)")
            if start.lower() == "y":
                break

    @staticmethod
    def end():
        print("Thank you for playing!")