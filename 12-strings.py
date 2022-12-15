## Strings


s = "hEllo"
print(s[0])
print(s[-1])
print(len(s))

count = s.count("l")
print(count)

find = s.find("l")
print(find)

upper = s.upper()
print(upper)

lower = s.lower()
print(lower)

capital = s.capitalize()
print(capital)

contains = "h" in s
print(contains)

t = "19"
is_digit = t.isdigit()
print(is_digit)

u = "hello my name is Kresna"
words = u.split() # the default delimiter is space
print(words)

replace = u.replace('a', 'i')
print(replace)
print(u)