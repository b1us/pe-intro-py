# Dictionaries
# A dictionary is a collection which is unordered, changeable and indexed. 
# As of Python version 3.7, dictionaries are `ordered`. In Python 3.6 and earlier, dictionaries were `unordered`.
# In Python dictionaries are written with curly brackets, and they have `keys`` and `values` pair.
# We can add, remove, change, and look up the values of the dictionary.
# Syntax: {key1: value1, key2: value2, key3: value3, ...}
# Keys must be unique, and the values can be of `any` data type.
# We can access the items of a dictionary by referring to its key name, inside square brackets.
# We can change the value of a specific item by referring to its key name.
# We can loop through a dictionary by using a `for` loop.
# We can check if a key exists by using the `in` keyword.
# We can determine how many items (key-value pairs) a dictionary has by using the `len()` function.
# We can add items to the dictionary by using a new index key and assigning a value to it.
# We can remove items from the dictionary by using the `del` keyword, or the `pop()` method.
# The `popitem()` method removes the last inserted item (in versions before 3.7, a random item is removed instead).
# The `clear()` method empties the dictionary.
# The `copy()` method makes a copy of a dictionary.
# The `update()` method updates the dictionary with the items from a given argument.
# The `fromkeys()` method returns a dictionary with the specified keys and the specified value.
# The `get()` method returns the value of the specified key.
# The `items()` method returns a list containing a tuple for each key value pair.
# The `keys()` method returns a list containing the dictionary's keys.
# The `values()` method returns a list of all the values in the dictionary.
# The `setdefault()` method returns the value of the specified key. If the key does not exist: insert the key, with the specified value.

x = {2: "hello", "1": 5}
print(x)
print(x[2])

y = {"name": "John", "age": 36}
print(y)
print(y["age"])

# Add a new item to the dictionary
# syntax: dict[key] = value
z = {} # empty dictionary => {} or dict()

z["name"] = "Adi"
z["age"] = 7
print(z)

# Add an item to the dictionary that already exists => the value will be overwritten (updated)
z["name"] = "Bagus"
z["hoby"] = "soccer"
print(z)

# Access the items of a dictionary by referring to its key name, inside square brackets
print(z["name"])

# If we access a key that does not exist, we get an error => KeyError
# print(z["address"]) # KeyError: 'address'

# Delete an item from the dictionary
del z["hoby"]
print(z)

# Check if a key exists in the dictionary by using the `in` keyword => return True or False 
# (not the value)
if "name" in z:
    print("Yes, 'name' is one of the keys in the z dictionary")
if "address" in z:
    print("Yes, 'address' is one of the keys in the z dictionary")

# dict_values() => list of values in the dictionary (unique in Phython 3.7)
# values() method returns a list of all the values in the dictionary
print(z.values()) # dict_values(['Bagus', 7])
# if we want to access the item, we need to convert it (dict_value) to a list first using list function
print(list(z.values())) # ['Bagus', 7]

# dict_keys() => list of keys in the dictionary (unique in Phython 3.7)
# keys() method returns a list containing the dictionary's keys
print(z.keys()) # dict_keys(['name', 'age'])
# if we want to access the item, we need to convert it (dict_keys) to a list first using list function
print(list(z.keys())) # ['name', 'age']
