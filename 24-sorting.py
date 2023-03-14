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