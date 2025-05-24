# Lesson 08: Control Modules & Functions

# Function definition
# Functions are reusable blocks of code that perform a specific task.
def greet(name):
    print(f"Hello, {name}!")

greet("Ali")

# Function with default argument
# If no argument is passed, the default value is used.
def greet_default(name="Guest"):
    print(f"Welcome, {name}!")

greet_default()

# Function with return value
# Returns a value to the caller.
def add(a, b):
    return a + b

result = add(3, 4)
print("Sum:", result)

# Importing Modules
# Modules are files containing reusable Python code.
import math
print("Square root of 16:", math.sqrt(16))

from math import pow
print("2 power 3:", pow(2, 3))


# Lesson 09: Exception Handling

# Try-Except Block
# Used to catch and handle runtime errors.
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
finally:
    print("This block always executes.")

# Raising Exceptions
# Used to throw an exception manually.
def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18.")
    return "Access granted"

try:
    print(check_age(16))
except ValueError as e:
    print("Error:", e)


# Lesson 10: File Handling

# Writing to a file
# Opens file for writing (creates if not exists).
with open("example.txt", "w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("Second line.")

# Reading from a file
# Opens file in read mode.
with open("example.txt", "r") as f:
    content = f.read()
    print("File content:")
    print(content)

# Appending to a file
# Adds content to the end of the file.
with open("example.txt", "a") as f:
    f.write("\nAppended line.")

# Reading line by line
# Useful for large files.
with open("example.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())


# Lesson 11: Math, DateTime & Calendar

# Math Module
# Provides mathematical functions.
import math
print("Ceil of 4.3:", math.ceil(4.3))       # Round up
print("Floor of 4.7:", math.floor(4.7))     # Round down
print("Factorial of 5:", math.factorial(5)) # Multiply all whole numbers up to 5

# DateTime Module
# Used to work with dates and times.
import datetime
now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year, "Month:", now.month)

# Calendar Module
# Used to view and work with calendar-related tasks.
import calendar
print("Is 2024 a leap year:", calendar.isleap(2024))
print("Calendar of May 2025:")
print(calendar.month(2025, 5))
