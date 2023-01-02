# While Loops
# Iterate whie a condition is true.
# Not knowing the number of iterations in advance. 
# Contrast to For Loops, which iterate a fixed number of times.
x = 0
while x < 5:
    x += 1
    print("x is", x)

# Compound
# The compound assignment operators can be used in a while loop.
y = 0
while y < 10 and y % 2 == 0:
    y += 1
    print("y is", y)