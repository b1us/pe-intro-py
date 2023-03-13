# Math
#
# abs()	Returns the absolute value of a number
x = abs(-9)
print(x) # 9

y = abs(9.5)
print(y) # 9.5

# max()	Returns the largest item in an iterable
x = max(1, 2, 3, 4, 5)
print(x) # 5

y = max([1, 2, 3, 4, 5])
print(y) # 5

z = max("Hello World")
print(z) # r

# min()	Returns the smallest item in an iterable
x = min(1, 2, 3, 4, 5)
print(x) # 1

y = min([1, 2, 3, 4, 5])
print(y) # 1

z = min("Hello World")
print(z) #   (space)

# sum()	Sums the items of an iterable
x = sum([1, 2, 3, 4, 5])
print(x) # 15

y = sum((1, 2, 3, 4, 5))
print(y) # 15

z = sum({1, 2, 3, 4, 5})
print(z) # 15

a = sum(1, 2, 3, 4, 5)
# print(a) # TypeError: sum expected at most 2 arguments, got 5 (it's not iterable)

# round()	Rounds a numbers
x = round(9.51)
print(x) # 10

y = round(9.49)
print(y) # 9

z = round(9.49, 1) # 1 is the number of decimals
print(z) # 9.5

a = round(9.494, 2)
print(a) # 9.49