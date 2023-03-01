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

# Example tuple
g = (1, 2, 3)
# g[0] = 4 # TypeError: 'tuple' object does not support item assignment because tuple is `immutable`

# List and function
# List is mutable, so it can be changed inside a function.
def add_to_list(lst, item):
    lst.append(item) # be careful! it's directly modifying the list inside the function
    # print(lst) # [1, 2] # modifying object in place

h = []

add_to_list(h, 1)
add_to_list(h, 2)
print(h) # [1, 2]

# Example dictionary
i = {}
i['k'] = 'v'

j = i
j['k2'] = 'v2'

print(j, i) # {'k': 'v', 'k2': 'v2'} {'k': 'v', 'k2': 'v2'} # same object # affects the original object

# Example set
k = set()
l = k

k.add(1)
l.add(2)

print(k, l) # {1, 2} {1, 2} # same object # affects the original object
print(k is l) # True

def add_to_set(s, item):
    s.add(item) # be careful! it's directly modifying the set inside the function
    # print(s) # {1, 2} # modifying object in place

m = set()
add_to_set(m, 1)
print(m) # {1}

# Copying a mutable object
# To copy a mutable object into a new object, 
# We can use the `copy` module or use slicing.
# `copy` module has `copy` and `deepcopy` functions.
# `copy` function creates a shallow copy of an object.
# `deepcopy` function creates a deep copy of an object.
# A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
# A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
# (https://docs.python.org/3/library/copy.html)


# Copy by slicing in list
n = [1, 2, 3]
o = n[:] # copy by slicing
n.append(4)
print(n, o) # [1, 2, 3, 4] [1, 2, 3]

# Copy in set and dictionary, we can use `copy` module
set1 = {1, 2, 3}
set2 = set1.copy() # shallow copy

set1.add(4)
print(set1, set2) # {1, 2, 3, 4} {1, 2, 3}

dict1 = {'k': 'v'}
dict2 = dict1.copy() # shallow copy

dict1['k2'] = 'v2'
print(dict1, dict2) # {'k': 'v', 'k2': 'v2'} {'k': 'v'}