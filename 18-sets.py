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


