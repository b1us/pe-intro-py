# Interface

# An interface is a contract that a class can implement to conform to a standard way of providing certain kinds of functionality.
# It is a 100% abstract class that contains only abstract methods and static methods.
# (It's really like abstract class but only contain abstract methods)
# Contains no implementation details, no code other than definition of methods and also raise `NotImplementedError` inside every those methods.
# The point of `Interface` is only define and describe all the methods that must be implemented by any class that inherits from it.
# It's really important in `static type` languages like Java, but not that important in Python.
# In Python we can achieve the same thing but not trully an interface.

# Interface examples

# Example
class RunCodeInterface: # do not needed to create `Interface` class name, just for education purpose only
    def compile_code(self):
        raise NotImplementedError("You must provide an implementation for compile_code() method") 
        # do not to put any message, but it is good practice to explain why it is raised

    def execuete_code(self):
        raise NotImplementedError("You must provide an implementation for execuete_code() method")

# In other language, inherit class from an Interface would look like this:
# class GoCode implements RunCodeInterface:
# but in Phyton, since no real `interface` we would go with something like this:

class GoCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Go Code")
    
    def execute_code(self):
        print("Execute Go Code")

class JavaCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Java Code")
    
    def execute_code(self):
        print("Execute Java Code")

# Different from strong type language, in Python the parameter type is not enforced,
# only the interface/abstract methods need to be implemented
def run_code(code : RunCodeInterface):
    code.compile_code()
    code.execute_code()

go = GoCode()
run_code(go)

java = JavaCode()
run_code(java)