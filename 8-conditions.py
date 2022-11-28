## conditions
# compare int and float works
# == != < > <= >=
# arithmetic first follows by comparison
# comparing for equivalency of string: capitalization and space matters
# comparing for non equivalency of string: using ASCII characters (numeric representation) 
# ordinal function ord() and character function chr()
# mutliple characters compared in orders
# comparing bool with other types works differently, re-check it against others
# different types comparison doesn't work, except for equivalent / non equivalent check

cond1 = 2 == 3
cond2 = 3.0 == 3
cond3 = 4 != 5
x = 6
y = 7
str1 = "hello"
str2 = "hello"
str3 = "Hello"
str4 = "hello "
cond4 = x != y
cond5 = x + 2 > 9
cond6 = x == str1
cond7 = str1 == str2
cond8 = str1 == str3
cond9 = str1 == str4
print("1", cond1)
print("2", cond2)
print("3", cond3)
print("4", cond4)
print("5", cond5)
print("6", cond6)
print("7", cond7)
print("8", cond8)
print("9", cond9)
print(ord('a'))
print(chr(65))
print("10", True == 1)
print("11", False == 0)
print("12", False == 4)
print("13", False == "a")
print("14", True == "")
cond = "hello " < "lz"
print("15", cond)