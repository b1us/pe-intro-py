## Conditionals
# if / elif / else
# indentation matters

name = input("Name: ")

if name == "K":
    print("Hello K!")
elif name == "L":
    print("Hello L!")
elif name == "M":
    print("Hello M!")
else:
    print("Hello there!")

# Compound conditions and nested conditions

number = float(input("Number: "))

if number > 0 and number % 2 == 0:
    print("This is a positive even number")

    number2 = float(input("Number2: "))
    if number2 < 0:
        print("This is a negative number")
    else:
        print("This is a positive number")

# In-line conditions
x = 5

result = "Ok" if x == 5 else "Not Ok"
print(result)
print("Ok") if x > 5 else print("Not Ok")