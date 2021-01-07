# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

num1 = int(input("What is the first number you would like to compute: "))
num2 = int(input("What is the second number you would like to compute: "))
def calculator(num1, num2):
    operation = input("What would you like to do? + / * or -: ")
    if operation == '+':
        return print(num1 + num2)
    if operation == '-':
        return print(num1 - num2)
    if operation == '*':
        return print(num1 * num2)
    if operation == '/':
        return print(num1 / num2)
    else:
        print("An invalid operator was entered closing program")

calculator(num1, num2)