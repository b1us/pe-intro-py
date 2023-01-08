# Slices
# An operator that can be used on any collection data types such as strings, lists, tuples, and dictionaries.
# Allows as to create sub-sets of the original collection that contains a specific element or a range that we want.
# Syntax: [start:stop:step]
# start: the index of the first element that we want to `include in the slice
# stop: the index of the first element that we want to `exclude` from the slice
# step: the number of elements that we want to skip between each element that we include in the slice
# If we don't specify a start index, Python will assume that we want to start at the beginning of the collection.
# If we don't specify a stop index, Python will assume that we want to stop at the end of the collection.
# If we don't specify a step index, Python will assume that we want to include every element in the slice.
# If we don't specify any of the indices, Python will assume that we want to include every element in the slice.
# If we specify a negative index for the start, stop, or step, Python will count backwards from the end of the collection.
# If we specify a negative index for the start, Python will count backwards from the end of the collection.
# If we specify a negative index for the stop, Python will count backwards from the end of the collection.
# If we specify a negative index for the step, Python will count backwards from the end of the collection.
# If we specify a negative index for the start, stop, or step, Python will count backwards from the end of the collection.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_new_list = my_list[0:5] # [1, 2, 3, 4, 5]
print(my_new_list)
my_new_list2 = my_list[5:10] # [6, 7, 8, 9, 10]
print(my_new_list2)
my_new_list3 = my_list[0:10:2] # [1, 3, 5, 7, 9]
print(my_new_list3)
my_new_list4 = my_list[::2] # [1, 3, 5, 7, 9]
print(my_new_list4)
my_new_list5 = my_list[1::2] # [2, 4, 6, 8, 10]
print(my_new_list5)
my_new_list6 = my_list[1:10:2] # [2, 4, 6, 8]
print(my_new_list6)
my_new_list7 = my_list[1:10:3] # [2, 5, 8]
print(my_new_list7)
my_new_list8 = my_list[1:10:4] # [2, 6]
print(my_new_list8)
my_new_list9 = my_list[1:10:5] # [2, 7]
print(my_new_list9)
my_new_list10 = my_list[1:10:6] # [2, 8]
print(my_new_list10)
my_new_list11 = my_list[1:10:7] # [2, 9]
print(my_new_list11)
my_new_list12 = my_list[1:10:8] # [2]
print(my_new_list12)
my_new_list13 = my_list[1:10:9] # [2]
print(my_new_list13)
my_new_list14 = my_list[:6] # [1, 2, 3, 4, 5, 6]
print(my_new_list14)
my_new_list15 = my_list[-1] # 10
print(my_new_list15)
my_new_list16 = my_list[len(my_list):0:-1] # [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(my_new_list16)
my_new_list17 = my_list[::-1] # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (reverse the list)
print(my_new_list17)
my_new_list18 = my_list[:] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (copy of the list)
print(my_new_list18)

# Slice a string or other collection data structure
string = "Hello World"

print(string[::2]) # HloWrd
print(string[::-1]) # dlroW olleH (reverse the string)

# Slice a tuple
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # or also can be wrote as my_tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(my_tuple[::2]) # (1, 3, 5, 7, 9)
print(my_tuple[::-1]) # (10, 9, 8, 7, 6, 5, 4, 3, 2, 1) (reverse the tuple)
print(my_tuple) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) (original tuple is not changed)