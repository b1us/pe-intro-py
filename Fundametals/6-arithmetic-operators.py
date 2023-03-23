## arithmetic operations. 
# works for different numbers types like floats and integers
# floats operations to integers = floats

x = 2
y = 3
z = 4.5

result = x + y
result2 = x + z
print(result)
print(result2)

# operations
# substracton -
# multiply *
# division / the result will always be `floats`. Div by 0 will not work
# exponents **
# integer division // (rounds down)
# modulus %

# order operations (precedence)
# result = x % y + 4 - 7 ** (2 / 3) as follows
# brackets/parenthesis
# exponents
# multiplication and divisio and modulus
# additions and substractions

# operations on different data types 
# `integer` with `string`` = errors (TypeError)
# `int` with `True` = works => because True = 1; 
# `int` with `False`= error => because false = 0 => ZeroDivisionError
