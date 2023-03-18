# Sorting
#
# sorted() returns a new sorted list from the items in iterable.
# .sort() sorts the list in place.
#
lst = [1, 3, 2, 6, 8, 5, 9, 1, 4, 7, 1]
lst.sort() # sort the list in place
print(lst) # [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst2 = [1, 3, 2, 6, 8, 5, 9, 1, 4, 7, 1]
print(sorted(lst2)) # returns a new sorted list from the items in iterable
print(lst2) # [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9] (original list is unchanged)

# by default, sort() and sorted() sort in ascending order
# to sort in descending order, use reverse=True
lst.sort(reverse=True)
print(lst) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1] (original list is changed)

print(sorted(lst2, reverse=True)) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1]
print(lst2) # [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9] (original list is unchanged)

# sort a tuple
tup = (1, 3, 2, 6, 8, 5, 9, 1, 4, 7, 1)
print(sorted(tup)) # [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9] (returns a list) so we need to convert it back to a tuple
print(tuple(sorted(tup))) # (1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9) (returns a tuple)
print(tup) # (1, 3, 2, 6, 8, 5, 9, 1, 4, 7, 1) (original tuple is unchanged)

# we can not do sort() on a tuple
# tup.sort() # AttributeError: 'tuple' object has no attribute 'sort'

# Sort based on a key
# sort() and sorted() take a key argument that specifies a function to be called on each list element prior to making comparisons.
# The key specified here should be a function that takes a single argument and returns a key to use for sorting purposes.
# This technique is fast because the key function is called exactly once for each input record.
# The key function can also be used to extract a portion of the element being sorted, which can be used to sort complex objects.
# The key function can also be used to perform custom comparisons, such as case-insensitive string comparison.
# The key function can also be used to sort objects of different types, such as sorting a list of strings and integers together.
# The key function can also be used to sort objects of different types, such as sorting a list of strings and integers together.
# Example: sort a list of strings by their length
lst3 = ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg']
print(sorted(lst3, key=len)) # ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg']
print(lst3) # ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg'] (original list is unchanged)

# Example: sort a list of strings by their length in descending order
print(sorted(lst3, key=len, reverse=True)) # ['ggggggg', 'ffffff', 'eeeee', 'dddd', 'ccc', 'bb', 'a']
print(lst3) # ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg'] (original list is unchanged)

lst4 = [[3, 2], [1, 2], [9, 10], [5, 6], [-1, 22], [0, 0]]
# sort by the first element of each sublist
print(sorted(lst4)) # [[-1, 22], [0, 0], [1, 2], [3, 2], [5, 6], [9, 10]] (returns a new sorted list)
lst4.sort()
print(lst4) # [[-1, 22], [0, 0], [1, 2], [3, 2], [5, 6], [9, 10]] (original list is changed)

# sort by the second element of each sublist
def second_element(item):
    return item[1]
print(sorted(lst4, key=second_element)) # [[0, 0], [1, 2], [3, 2], [5, 6], [9, 10], [-1, 22]] (returns a new sorted list)

