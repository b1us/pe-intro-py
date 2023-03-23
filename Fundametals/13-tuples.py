# Tuples
# zero-indexing
# can not directly modified (imutable)
# keyword: tuple()
tup = (1, True, "string")
count = tup.count(1)
index = tup.index("string")
contains = 1 in tup
print(tup)
print(count)
print(index)
print(contains)

# nested tuples
x = (1, 2, (3, 4), True, [])
print(x[2][1])

# multiply and add tuples
y = (1, 2, 3)
z = (4, 5, 6)
combined = y + z
print(combined) 
multiplied = y * 3
print(multiplied)

a = (1, 2, 3)
b = (a[0], 4, a[2])
print(a)
print(b)