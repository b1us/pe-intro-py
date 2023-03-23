## List
# data type that stores an ordered collection of elements
# can contain different types
# use index to store and access
# methods: append(), pop(), count(), index(), remove(), extend(), list(),

list1 = []
list2 = [1, 2.5, True, "string", ["another list"]]
print(list2[4])
list2[2] = False
print(list2)
list2.append("append this") 
print(list2)
length = len(list2)
print(length)

s = "hello"

print(s[0]) # string as a collection of ellement except can not be assigned any new element nor be appended

# in
list_contains_5 = 5 in list2
print(list_contains_5)

# negative index
list_negative_one = list2[-5] # reversed
print(list_negative_one)

# combine list
x = [1, 2, 3]
y = ["a", "b"]
z = [1, 2]
combined = x + y # create a new list
print(combined)


a = [1, 2, 3]
b = [1, 2]
print(a.extend(b))
print(b.extend(a))

# multidimensional (nested) list
lst = [[5, 6, ["a", "b"]], [10], [1, 2, 3]]
print(lst[0][2][0])