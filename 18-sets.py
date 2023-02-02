# Sets
# Definition of a set is a collection of unique elements in no particular order 
# Sets are mutable, but the elements must be immutable
# Sets are unordered, so you cannot access items using indexes
# Syntax: set_name = {item1, item2, item3, ...}

# Create a set
set1 = {1, 2, 3, 4, 5}
print(set1)

# Create an empty set
x = set() # it becomes x = {}, don't be confused with dictionary
y = {} # it becomes empty dictionary y = {}
z = {1, 2, 3} # it becomes set z = {1, 2, 3} as soon as we add some value in it
print(type(x))
print(type(y))
print(type(z))

# Add an item / property to a set
# Syntax: set_name.add(item)
# If the item already exists, it will not be added
# If the item does not exist, it will be added
a = {1, 2, 2, 2, 3, 1, 4, 4}
print(a) # it will print {1, 2, 3, 4}
a.add(5)
print(a) # it will print {1, 2, 3, 4, 5}
a.add(5)
print(a) # it will print {1, 2, 3, 4, 5} as 5 already exists

# Remove an item / property from a set
# Syntax: set_name.remove(item)
# If the item does not exist, it will raise an error
# If the item exists, it will be removed
b = {1, 2, 3, 4, 5}
print(b) # it will print {1, 2, 3, 4, 5}
b.remove(5)
print(b) # it will print {1, 2, 3, 4}
# b.remove(5) # it will raise an error as 5 does not exist

# Clear a set
# It will remove all the items from the set
# Syntax: set_name.clear()
c = {1, 2, 3, 4, 5}
print(c) # it will print {1, 2, 3, 4, 5}
c.clear()
print(c) # it will print set()

# Length of a set
# It will return the number of items in the set
# Syntax: len(set_name)
d = {1, 2, 3, 4, 5}
print(len(d)) # it will print 5
e = {3, True, False, "hello", "world", 0,2, (1, 2, 3)}
print(len(e)) # it will print 9
# You can not add a list or dictionary to a set as they are mutable. Tuple is fine as it is immutable
# e = {3, True, False, "hello", "world", 0,2, (1, 2, 3), [1, 2, 3], {"name": "John", "age": 36}}
# print(len(e)) # it will raise an error (unhased type: 'list' or 'set' or 'dictionary') as list, set and dictionary are mutable

# Find an item in a set
# It will return True if the item exists in the set, otherwise it will return False
# Syntax: item in set_name
f = {1, 2, 3, 4, 5}
print(1 in f) # it will print True

# Union of two sets
# It will return a new set containing all items from both sets
# The duplicate items will be removed
# Syntax: set_name1.union(set_name2)
g = {1, 2, 3, 4, 5}
h = {4, 5, 6, 7, 8, 9, 10}

i = g.union(h)
print(i) # it will print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(g) # it will print {1, 2, 3, 4, 5}
print(h) # it will print {4, 5, 6, 7, 8, 9, 10}

# Shorter way to union two sets / union shortcut
# syntax: set_name1 | set_name2
j = g | h
print(j) # it will print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Intersection of two sets
# It will return a new set containing only the items that exist in both sets
# Syntax: set_name1.intersection(set_name2)
k = g.intersection(h)
print(k) # it will print {4, 5}

# Shorter way to find intersection of two sets / intersection shortcut
# syntax: set_name1 & set_name2
l = g & h
print(l) # it will print {4, 5}

# Difference of two sets
# It will return a new set containing only the items that exist in the first set, but not in the second set
# The original sets will remain unchanged
# Syntax: set_name1.difference(set_name2)
m = g.difference(h)
print(m) # it will print {1, 2, 3}
# The sortcut for difference is -
# syntax: set_name1 - set_name2
n = g - h
print(n) # it will print {1, 2, 3}

# Different result of the way we use difference
o = h - g
print(o) # it will print {6, 7, 8, 9, 10}

# Symmetric difference of two sets
# It will return a new set containing only the items that exist in either set, but not in both
# The original sets will remain unchanged
# Syntax: set_name1.symmetric_difference(set_name2)
p = g.symmetric_difference(h)
print(p) # it will print {1, 2, 3, 6, 7, 8, 9, 10}

# Shorter way to find symmetric difference of two sets / symmetric difference shortcut
# syntax: set_name1 ^ set_name2
q = g ^ h
print(q) # it will print {1, 2, 3, 6, 7, 8, 9, 10}