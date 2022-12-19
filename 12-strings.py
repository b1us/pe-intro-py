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

# f string => 3.6
name = "Tim"
t = f"Hello, {name}! You are {t} years old."
print(t)

# string multiplication
print(name * 5)

# multi line string (looks like multi line comment, but it has to be assigned to a string variable)
multiline_string_double_quotation = """
hello, my name is Kresna
this is a double quotation multi line string
and see you on the next section!
"""
print(multiline_string_double_quotation)

multiline_string_single_quotation = '''
hello, my name is Kresna
this is a single quotation multiline string
and see you on the next section!
'''
print(multiline_string_single_quotation)

# escape character (backslash)
string1 = f"{name}'s"
string2 = f'{name}"s'
string3 = f"{name}\"s"

print(string1)
print(string2)
print(string3)