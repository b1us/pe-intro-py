# For Loops
#
# For loops are used to iterate over a sequence of values.
# The syntax is:
# for <variable> in <sequence>:
#     <statements>
# The variable is assigned each value in the sequence in turn.
# The statements are executed once for each value in the sequence.
# The statements are indented to show that they are part of the loop.
# The indentation is important - Python uses indentation to show
# which statements are part of a loop or a function.
#
# The range function returns a sequence of numbers.
# The syntax is:
# range(<start>, <stop>, <step>)
# range(<start>, <stop>)
# range(<stop>)
# The start is the first number in the sequence.
# The stop is one more than the last number in the sequence.
# The step is the difference between each number in the sequence.
# The range(<start>, <stop>, <step>) function creates an interator that returns integers from `start`` (inclusive) to `stop` (exclusive), incrementing the las value by `step` every time.
# The default start is 0.
# The default step is 1.
# The default stop is the start.
for i in range(5):
    print("for i in range 5", i)

for i in range(2, 5):
    print("for i in range (2, 5)", i)

for i in range(2, 10, 2):
    print("for i in range (2, 10, 2)", i)

# The range function can be used to iterate over a sequence of values in an array/list. 
lst = [1, 2, 3, 4, 5, True, False]
for i in range(len(lst)): # (iterating by index)
    print(lst[i])

# Re-write the above loop using a for loop. Downside is that you can't use the index (iterating by element)
for i in lst:
    print(i)

# `Enumrate keyword` returns the index and the value of the list. (iterating by index and element)
for idx, val in enumerate(lst):
    print("index: ", idx, "value: ", val)

# Break and Continue
# The break statement can be used to exit a loop.
# The continue statement can be used to skip the rest of the loop.
for i in range(10):
    if i == 5:
        break
    print("from break", i)

for i in range(10):
    if i == 5:
        continue
    print("from continue", i)

# Nested For Loops
# For loops can be nested.
# The inner loop is executed once for each value in the outer loop.
for i in range(3):
    for j in range(5):
        for k in range(2):
            print("i = ", i, "j = ", j, "k = ", k)

# Nested for loops on lists
lst1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
for i in range(len(lst1)):
    inner_list = lst1[i]
    for j in range(len(inner_list)):
        print(inner_list[j])

for i in range(len(lst1)):
    for j in range(len(lst1[i])):
        print(lst1[i][j])

for i in lst1:
    for j in i:
        print(j)


# Some more examples
# Is `w` exist in the string?
st = "Hello world"

for i, char in enumerate(st):
    if char == "w":
        print("w => index:", i)
        break
else:
    print("w does not exist in the string")
    
# Ask a user to enter a number between 1 and 10. If the user enters a number outside of the range, ask them to try again until they enter a valid number. Print the result.
numbers = []

for i in range(3):
    num = int(input("Enter a number between 1 and 10: "))

    # if num < 1 or num > 10:
    #     print("Try again, remember the number should be between 1 and 10")
    # else:
    numbers.append(num)

print("Thank you. Here are your numbers:")
print(numbers)

# Pass
# The pass statement does nothing.
# It is used as a placeholder when a statement is required syntactically but the program requires no action.
for i in range(10):
    pass

# For else
# The else clause is executed after the loop completes normally.
# The else clause is not executed if the loop is exited with a break statement.
words = ("cat", "dog", "bird", "fish", "snake", "lizard", "horse", "cow", "pig", "chicken")
target= "snake"

for word in words:
    if target:
        print("Target found: ", target)
        break
else:
    print("Loop completed normally")
