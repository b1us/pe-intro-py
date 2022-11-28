## type conversions
# example: string -> integer <-> float
x = "4"
y = int(x) + 4
z = float(x) + 4
a = str(0)
print(type(x))
print(type(y))
print(type(z))
print(type(a))

# bool -> empty string = false, otherwise = true,
# bool -> int 0 = false, otherwise = true,
