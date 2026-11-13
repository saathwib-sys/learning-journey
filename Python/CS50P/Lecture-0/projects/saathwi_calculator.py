
# =====================================================
# PROJECT: SAATHWI'S PERSONAL CALCULATOR
# Course: CS50P - Lecture 0
# Created by: Saathwi
# =====================================================


# -----------------------------------------------------
# FUNCTION 1 - PERSONALIZED GREETING
# -----------------------------------------------------

def greet(first, middle, last):

    # Remove surrounding whitespace
    first = first.strip().title()
    middle = middle.strip().title()
    last = last.strip().title()

    # Combine the names
    full_name = first + " " + middle + " " + last

    # Display a personalized greeting
    print(f"\nHello, {full_name}!")
    print("Welcome to Saathwi's Calculator!")


# -----------------------------------------------------
# FUNCTION 2 - ADDITION
# -----------------------------------------------------

def add(a, b):
    return a + b


# -----------------------------------------------------
# FUNCTION 3 - SUBTRACTION
# -----------------------------------------------------

def subtract(a, b):
    return a - b


# -----------------------------------------------------
# FUNCTION 4 - MULTIPLICATION
# -----------------------------------------------------

def multiply(a, b):
    return a * b


# -----------------------------------------------------
# FUNCTION 5 - DIVISION
# -----------------------------------------------------

def divide(a, b):
    return a / b


# -----------------------------------------------------
# FUNCTION 6 - REMAINDER
# -----------------------------------------------------

def remainder(a, b):
    return a % b


# -----------------------------------------------------
# FUNCTION 7 - FLOOR DIVISION
# -----------------------------------------------------

def floor_division(a, b):
    return a // b


# -----------------------------------------------------
# MAIN FUNCTION
# -----------------------------------------------------

def main():

    # Collect personal information
    print("================================")
    print("       SAATHWI'S CALCULATOR")
    print("================================")

    first = input("Enter your first name: ")
    middle = input("Enter your middle name: ")
    last = input("Enter your last name: ")

    # Call the greeting function
    greet(first, middle, last)

    # Collect two numbers
    print("\n------ ENTER TWO NUMBERS ------")

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    # Perform mathematical operations
    print("\n------ CALCULATION RESULTS ------")

    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {subtract(x, y)}")
    print(f"Multiplication: {multiply(x, y)}")

    # Division operations require a nonzero divisor
    if y != 0:
        print(f"Division: {divide(x, y):.2f}")
        print(f"Remainder: {remainder(x, y)}")
        print(f"Floor division: {floor_division(x, y)}")
    else:
        print("Division: Cannot divide by zero.")
        print("Remainder: Cannot divide by zero.")
        print("Floor division: Cannot divide by zero.")

    print("\n================================")
    print(" Thank you for using my calculator!")
    print("================================")


# Start the program
main()
