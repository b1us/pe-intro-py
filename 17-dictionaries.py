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

# dict_items() method returns a list containing a tuple for each key value pair
print(z.items()) # dict_items([('name', 'Bagus'), ('age', 7)])
# if we want to access the item, we need to convert it (dict_items) to a list first using list function
print(list(z.items())) # [('name', 'Bagus'), ('age', 7)]

# Length of the dictionary
print(len(z)) # 2

# Iterate through the dictionary
# We can loop through a dictionary by using a `for` loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# Dictionary items are unordered, meaning: we cannot be sure in which order the items will appear.
for x in z:
    print(x) # name age

# We can not rely on the order of the items when we use a dictionary, as they are unordered, changeable, and does not allow duplicate values.
# If we wan to accessing an index in a dictionary, we need to use the key instead of the index number.
# We can access the items of a dictionary by referring to its key name, inside square brackets.
# So we need to loop through the dictionary using/by the keys() method to access the values.
for key in z:
    value =  z[key]
    print(key, value) # name Bagus age 7
# or decompose the for loop by tuple unpacking
for key, value in z.items():
    print(key, value) # name Bagus age 7

# The `get()` method returns the value of the specified key.
# If the key does not exist, return None
# It's also possible to add a default value to the `get()` method
# If the key does not exist, return the default value

print(z.get("name")) # Bagus
print(z.get("address")) # None
print(z.get("address", "Bali")) # Bali

# Frequency of the characthers in the string
characthers = {}

string = "Hello World"

for char in string:
    characthers[char] = characthers.get(char, 0) + 1
print(characthers) # {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}

# Another example, to count how many times each character is being inputed by the user
count = {}

while True:
    num = input("Enter a number (enter q to quit): ")
    if num == "q":
        break
    num = int(num)
    count[num] = count.get(num, 0) + 1

print(count)

# time complexity of the dictionary is O(1) => constant time
# the dictionary is implemented using a hash table
# in the other hand, the list is implemented using an array
# time complexity of the list is O(n) => linear time
d = {"a": 1, "b": 1, "c": 1, "d": 1} # "d" in d => time complexity is O(1), very fast
l = ["a", "b", "c", "d"] # "d" in l => time complexity is O(n), takes longer time
