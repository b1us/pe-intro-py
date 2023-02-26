# Mutability
#
# Mutability of objects, specifically in data types.
#
# In Python, there are two types of objects: mutable (changeable) and immutable (not changeable).
#
# Immutable objects are those that cannot be changed after they are created.
# Immutable objects include `int`, `float`, `str`, `bool`, and `tuples`. And also `None` (special data type).
#
# Mutable objects are those that can be changed after they are created.
# Mutable objects include `list`, `dict`, and `set`.

x = 5 # object 5 is immutable
x += 1 # brand new object 6 is created
print(x) # 6

a = 1
b = a
a += 1
print(a, b) # 2 1 # a and b are two different objects

# list
a = [1, 2, 3]
b = a
a.append(4)
print(a, b) # [1, 2, 3, 4] [1, 2, 3, 4] # a and b are the same object

# to know if two objects are the same object
print(a is b) # True # is operator checks if two objects are the same object (it is not the same as == `equivalent` operator)
# but below is not the same object
c = []
d = []
print(c is d) # False # two different objects
print(c == d) # True # equivalent

# Id function returns the identity of an object (the memory address of the object) in base 10.
e = 1
f = 1
print(id(a), id(b)) # 1400000000000 1400000000000
print(id(c), id(d)) # 1400000000001 1400000000002
print(id(e), id(f)) # 1400000000003 1400000000003 # same object because of the optimization of Python (integers from -5 to 256 are cached) 
# (https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong) 
# (https://stackoverflow.com/questions/306313/is-operator-behaves-unexpectedly-with-integers) 
# (https://stackoverflow.com/questions/306313/is-operator-behaves-unexpectedly-with-integers/306332#306332)