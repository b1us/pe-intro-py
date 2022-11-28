## Compound Conditions
# Logical Operators
# `and` => True if `both` lhs and rhs (or `all` of them in multiple conditions) are `True`
# `or` => True if `any` of lhs and rhs (or `any` of them in multiple conditions) are `True`. 
# Only if `both` (or `all` of them in multiple conditions) are `False`
# `not` => reverse or swap 
# lowest precedence compared to other logical operators

x = 2
y = 4

compound1 = x < y and y + 2 > 3
print("1", compound1)

compound2 = x < y or y + 2 > 3
print("2", compound2)

compound3 = not (x < y)
compound4 = not True == False
# compound = True == not False (doesn't work because `not` has lower precedence than `==`) workaround is put the `not` inside the parenthesis such that: compound = True == (not False)
print("3", compound3)
print("4", compound4)

compound5 = True or False and not True or False
print("5", compound5)

# Order work in such ways:
# Parenthesis
# Conditional / Comparison operators  (== != < > <= >=)
# not
# and
# or

## DeMorgan's Law / Boolean Algebra
# demorgan = not (x and y) == (not x) or (not y)
# demorgan2 = not (x or y) == (not x) and (not y)

# Truth Tables
