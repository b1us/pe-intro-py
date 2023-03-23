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

# Input Validation
# Use a while loop to validate user input.
# The input() function returns a string, so we need to convert it to an int.
# The int() function will throw an error if the string cannot be converted to an int.
# We can use a try/except block to catch the error and ask the user to try again.
# The while loop will continue to ask the user for input until a valid int is entered.

num = input("Enter a integer: ")

while not num.isdigit():
    print("That's not a integer!")
    num = input("Enter a integer: ")

# Another example  
z = 0
while True:
    try:
        z = int(input("Enter a number: "))
        break
    except ValueError:
        print("That's not a number!")

lst = [2, 3, 1, 2, 3, 4, 5]
result = 0
while result < 10:
    for i in lst:
        result += i
        print(result)
        if result > 10:
            break

lst2 = [2, 3, 3, -2, -2, 1]
i = 0

while i < len(lst2):
    num = -2
    if lst2[i] == num:
        print("found the number", num)
        break
    i += 1
else:
    print("did not find the number", num)

lst3 = [2, 3, 3, -2, -2, 1]
i = 0

while i < len(lst3):
    if lst3[i] < 0:
        lst3.pop(i)
    else:
        i += 1
print(f"lst3:", lst3)