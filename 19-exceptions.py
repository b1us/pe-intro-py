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
    print("An error occurred", e)