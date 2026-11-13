
# =====================================================
# CS50P - LECTURE 0
# INTERMEDIATE PRACTICE
# Student: Saathwi
# =====================================================


# -----------------------------------------------------
# Q1 - FUNCTION WITH A DEFAULT PARAMETER
# -----------------------------------------------------

# If no argument is passed, the default value is used.

def hello(to="world"):
    to = to.strip().title()
    print(f"Hello {to}!")


# Passing an argument
hello("saathwi")

# Not passing an argument
# The default value "world" will be used.
hello()


# -----------------------------------------------------
# Q2 - FUNCTION WITH MULTIPLE PARAMETERS
# -----------------------------------------------------

# A function can accept multiple arguments.

def sum_numbers(a, b, c):
    return a + b + c


result = sum_numbers(10, 20, 30)
print(f"Total: {result}")


# -----------------------------------------------------
# Q3 - DEFAULT ARGUMENT AND RETURN VALUE
# -----------------------------------------------------

# b has a default value of 10.
# If the caller provides another value for b,
# the supplied value will be used instead.

def calculate(a, b=10):
    result = a + b
    return result


x = calculate(5)
y = calculate(5, 20)

print(f"First: {x}")
print(f"Second: {y}")
print(f"Total: {x + y}")


# -----------------------------------------------------
# Q4 - DIFFERENCE BETWEEN PRINT AND RETURN
# -----------------------------------------------------

# print() displays a value but does not return it.
# return sends a value back to the caller.

def add_and_print(a, b):
    print(a + b)


def add_and_return(a, b):
    return a + b


# First function
result1 = add_and_print(10, 20)

# Second function
result2 = add_and_return(10, 20)

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")


# -----------------------------------------------------
# Q5 - FLOAT INPUT AND DECIMAL FORMATTING
# -----------------------------------------------------

# float() converts input into a floating-point number.
# :.2f displays exactly two decimal places.

def add(a, b):
    return a + b


def main_addition():
    x = float(input("Enter value of x: "))
    y = float(input("Enter value of y: "))

    print(f"The sum is {add(x, y):.2f}")


# -----------------------------------------------------
# Q6 - GREETING USING FIRST AND LAST NAME
# -----------------------------------------------------

# strip() removes extra whitespace.
# title() formats the names.
# Both names are combined into one string.

def greet(first, last):
    first = first.strip().title()
    last = last.strip().title()

    full = first + " " + last

    print(f"Namaste, {full}!")


def name_main():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")

    greet(firstname, lastname)


# -----------------------------------------------------
# Q7 - SQUARE AND CUBE USING FUNCTIONS
# -----------------------------------------------------

def square(n):
    return n * n


def cube(n):
    return n * n * n


def power_main():
    num = int(input("Enter a number: "))

    print(f"Square: {square(num)}")
    print(f"Cube: {cube(num)}")


# -----------------------------------------------------
# Q8 - MULTIPLE MATHEMATICAL FUNCTIONS
# -----------------------------------------------------

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def remainder(a, b):
    return a % b


def floor_division(a, b):
    return a // b


def calculator_main():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {subtract(x, y)}")
    print(f"Multiplication: {multiply(x, y)}")

    if y != 0:
        print(f"Division: {divide(x, y):.2f}")
        print(f"Remainder: {remainder(x, y)}")
        print(f"Floor division: {floor_division(x, y)}")
    else:
        print("Division by zero is not allowed.")


# -----------------------------------------------------
# MAIN FUNCTION
# -----------------------------------------------------

def main():

    print("\n--- Q5: FLOAT ADDITION ---")
    main_addition()

    print("\n--- Q6: NAME GREETING ---")
    name_main()

    print("\n--- Q7: SQUARE AND CUBE ---")
    power_main()

    print("\n--- Q8: CALCULATOR ---")
    calculator_main()


# Calling the main function
main()
