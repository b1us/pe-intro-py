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
# The default start is 0.
# The default step is 1.
# The default stop is the start.
for i in range(5):
    print("for i in range 5", i)

for i in range(2, 5):
    print("for i in range (2, 5)", i)

for i in range(2, 10, 2):
    print("for i in range (2, 10, 2)", i)
