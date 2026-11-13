
# =====================================================
# CS50P - LECTURE 0
# ADVANCED PRACTICE
# Student: Saathwi
# =====================================================


# -----------------------------------------------------
# Q1 - FUNCTION CALLS AND EXECUTION FLOW
# -----------------------------------------------------

# main() calls calculate().
# calculate() adds two numbers and returns the result.
# main() stores the returned value in result.

def calculate(a, b):
    result = a + b
    return result


def main():
    x = 10
    y = 20

    result = calculate(x, y)

    print(f"Result: {result}")


main()


# -----------------------------------------------------
# Q2 - DEFAULT ARGUMENTS AND RETURN VALUES
# -----------------------------------------------------

# b has a default value of 10.
# If a second argument is supplied, the default is ignored.

def calculate(a, b=10):
    result = a + b
    return result


def main():
    x = calculate(5)
    y = calculate(5, 20)

    print(f"First: {x}")
    print(f"Second: {y}")
    print(f"Total: {x + y}")


main()


# -----------------------------------------------------
# Q3 - DIFFERENCE BETWEEN PRINT() AND RETURN
# -----------------------------------------------------

# print() displays the result but returns None.
# return sends the result back to the caller.

def add(a, b):
    print(a + b)


def main():
    result = add(10, 20)

    print(f"Result: {result}")


main()


# -----------------------------------------------------
# Q4 - MULTIPLE FUNCTIONS WORKING TOGETHER
# -----------------------------------------------------

# calculate() performs the addition.
# display() rounds the returned result to two decimals
# and returns the formatted numeric value.
# main() coordinates both functions.

def calculate(a, b):
    return a + b


def display(result):
    result = round(result, 2)
    return result


def main():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    z = calculate(x, y)

    print(f"Total: {display(z)}")


main()


# -----------------------------------------------------
# Q5 - NAME FORMATTING USING MULTIPLE FUNCTIONS
# -----------------------------------------------------

# strip() removes surrounding whitespace.
# title() formats the names.
# The greeting function returns the final message.

def greet(first, last):
    first = first.strip().title()
    last = last.strip().title()

    full = first + " " + last

    return f"Namaste, {full}!"


def main():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")

    message = greet(firstname, lastname)

    print(message)


main()


# -----------------------------------------------------
# Q6 - SQUARE AND CUBE USING SEPARATE FUNCTIONS
# -----------------------------------------------------

def square(n):
    return n * n


def cube(n):
    return n * n * n


def main():
    num = int(input("Enter a number: "))

    x = square(num)
    y = cube(num)

    print(f"Square: {x}")
    print(f"Cube: {y}")


main()


# -----------------------------------------------------
# Q7 - COMPLETE CALCULATOR USING FUNCTIONS
# -----------------------------------------------------

# Each mathematical operation has its own function.
# main() calls these functions and displays their results.

def add(a, b):
    return a + b


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


def main():
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


main()
