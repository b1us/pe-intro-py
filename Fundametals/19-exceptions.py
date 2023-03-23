# Exceptions 
# 
# Used to handle errors in a program.
# 
# How to handle exceptions:
# try:
#     # code that might throw an exception
# except:
#     # code to handle the exception
# else:
#     # code to run if no exception was thrown
# finally:
#     # code to run no matter what
#

# Example 1
try:
    print(1 / 0)
except:
    print("An error occurred.")

# Accept specific exception
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("An error occurred:", e)

# Accept multiple exceptions
try:
    int("hello")
except ZeroDivisionError as e:
    print("Zero division error occurred:", e)
except ValueError as e:
    print("Value error occurred:", e)

try:
    print(1 / 0)
except (ZeroDivisionError, TypeError) as e:
    print("[Multi] An error occurred:", e)

# General / generic exception
try:
    print(1 / 0)
except Exception as e:
    print("[Generic] An error occurred:", e)

# Finally block
# It will run no matter what happens in the try block (whether an exception is raised or not) and the except block (whether an exception is handled or not) 
# It is used to clean up the code
try:
    print(1 / 0)
except Exception as e:
    print("[Finally] An error occurred:", e)
finally:
    print("The 'try except' is finished.")

# Raise an error
# raise ValueError("This is an error!")
 
# Raise an general exception
# raise Exception("This is an error!")

# Some examples
# Example 1
num1 = input("[num1]Enter a number: ")

if not num1.isdigit():
    raise ValueError("[num1]This is not a valid number!")

# Example 2
while True:
    num2 = input("[num2]Enter a number: ")
    try:
        num2 = float(num2)
        break
    except ValueError as e:
        print("[num2]This is not a valid float, try again!", e)

# Best practice: don't overuse general excepttion


# Runtime vs Compile time exceptions

# Runtime exceptions: exceptions that occur during the execution of a program
# Compile time exceptions: exceptions that occur during the compilation of a program

# Compiling: converting source code to machine code (binary code / executable code / bytecode) i.e the code that the computer can understand (from human readable code to machine readable code or from high level language to low level language)

# Errors that may occur during compilation are called compile time errors / exceptions
# For example: SyntaxError

# Errors that may occur during execution are called runtime errors / exceptions
# For example: ZeroDivisionError, ValueError, etc.