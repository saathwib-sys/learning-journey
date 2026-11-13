
# =====================================================
# CS50P - LECTURE 0
# BASIC PRACTICE
# Student: Saathwi BK
# =====================================================


# -----------------------------------------------------
# Q1 - VARIABLES
# -----------------------------------------------------

# Variables are used to store values.

name = "Saathwi"
age = 21

print(name)
print(age)


# -----------------------------------------------------
# Q2 - COMMENTS
# -----------------------------------------------------

# This is a single-line comment.
# Comments help explain the code.


# -----------------------------------------------------
# Q3 - INPUT FUNCTION
# -----------------------------------------------------

# input() is used to get information from the user.

# name = input("Enter your name: ")
# print(name)


# -----------------------------------------------------
# Q4 - DATA TYPES
# -----------------------------------------------------

# int represents an integer.
# float represents a decimal number.
# str represents a string.

x = 25
y = 3.14
z = "Python"

print(type(x))
print(type(y))
print(type(z))


# -----------------------------------------------------
# Q5 - F-STRINGS
# -----------------------------------------------------

# f-strings allow us to insert variables into strings.

name = "Saathwi"
print(f"Hello, {name}!")


# -----------------------------------------------------
# Q6 - STRING METHODS: strip() and title()
# -----------------------------------------------------

# strip() removes whitespace from the beginning
# and end of a string.

# title() capitalizes the first letter of each word.

name = "  saathwi shetty  "

name = name.strip()
name = name.title()

print(name)


# -----------------------------------------------------
# Q7 - STRING CONCATENATION
# -----------------------------------------------------

# The + operator joins strings together.

x = "10"
y = "20"

print(x + y)       # Output: 1020


# -----------------------------------------------------
# Q8 - TYPE CASTING
# -----------------------------------------------------

# int() converts a value into an integer.
# float() converts a value into a floating-point number.
# str() converts a value into a string.

x = "10"
y = "20"

x = int(x)
y = int(y)

print(x + y)       # Output: 30


# -----------------------------------------------------
# Q9 - ARITHMETIC OPERATORS
# -----------------------------------------------------

a = 20
b = 6

print(a + b)       # Addition: 26
print(a - b)       # Subtraction: 14
print(a * b)       # Multiplication: 120
print(a / b)       # Division
print(a % b)       # Remainder: 2


# -----------------------------------------------------
# Q10 - ROUND FUNCTION
# -----------------------------------------------------

# round() rounds a number to the specified
# number of decimal places.

number = 3.14159

print(round(number, 2))    # Output: 3.14


# -----------------------------------------------------
# Q11 - USER INPUT AND TYPE CASTING
# -----------------------------------------------------

# input() returns a string.
# Use int() to convert input into an integer.

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
#
# print(x + y)


# -----------------------------------------------------
# Q12 - NAME FORMATTING USING FUNCTIONS
# -----------------------------------------------------

def hello(to):
    to = to.strip().title()
    print(f"Hello, {to}!")


# -----------------------------------------------------
# Q13 - ADDITION USING A FUNCTION
# -----------------------------------------------------

def add(a, b):
    return a + b


# -----------------------------------------------------
# Q14 - SIMPLE HELLO FUNCTION
# -----------------------------------------------------

def greet():
    print("Hello, Saathwi!")


# -----------------------------------------------------
# Q15 - SQUARE FUNCTION
# -----------------------------------------------------

def square(n):
    return n * n


# -----------------------------------------------------
# ADDITIONAL PRACTICE - ADDING THREE NUMBERS
# -----------------------------------------------------

def sum_numbers(a, b, c):
    return a + b + c


# -----------------------------------------------------
# MAIN FUNCTION - RUNNING THE PROGRAMS
# -----------------------------------------------------

def main():

    # Q12 - Get and format the user's name
    name = input("Enter your name: ")
    hello(name)

    # Q13 - Add two integers
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    result = add(x, y)
    print(f"The sum is {result}")

    # Q14 - Call the hello function
    greet()

    # Q15 - Calculate the square of a number
    number = int(input("Enter a number: "))

    result = square(number)
    print(f"The square is {result}")

    # Additional practice - Sum of three numbers
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))
    c = int(input("Enter third value: "))

    print(f"The total is {sum_numbers(a, b, c)}")


# Calling the main function
main()
