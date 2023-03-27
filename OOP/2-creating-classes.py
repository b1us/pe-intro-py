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