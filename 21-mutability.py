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
