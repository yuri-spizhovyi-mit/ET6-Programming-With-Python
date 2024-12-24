"""Python Lesson: Modules
Introduction
A module in Python is a file containing Python code (functions, classes, and variables) that you can reuse across multiple programs. Modules help organize code, promote reuse, and enhance maintainability.

1. Importing Modules
Definition
You can use the import statement to include a module in your program.

Syntax
python
Copy code
import module_name
Example"""

import math
from math import sqrt, pi
import math as m
import random
import my_module
import requests
import math_operations
import calculator

# Use the math module
print(math.sqrt(16))  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793

"""2. Importing Specific Functions or Variables
Definition
Use from module_name import function_name to import specific functions, classes, or variables from a module.

Syntax

from module_name import function_name
"""
print(sqrt(16))  # Output: 4.0
print(pi)  # Output: 3.141592653589793

"""3. Using Aliases
Definition
You can assign an alias to a module or imported function for convenience.
import module_name as alias
from module_name import function_name as alias
Syntax"""


print(m.sqrt(25))  # Output: 5.0
"""4. Built-in Modules
Python comes with a rich set of built-in modules. Common examples include:

os: For interacting with the operating system.
sys: For interacting with the Python runtime.
random: For generating random numbers.
datetime: For working with dates and times.
Example
python
Copy code
"""


print(random.randint(1, 10))  # Output: Random number between 1 and 10

# Custom modules

print(my_module.greet("Alice"))  # Output: Hello, Alice!
print(my_module.pi)  # Output: 3.14159

"""6. Exploring Module Contents
Use the dir() function to list the contents of a module.

Example"""
print(dir(math))

"""7. Installing External Modules
Definition
Python’s pip (Python package installer) allows you to install third-party modules.

Syntax
bash
Copy code
pip install module_name
Example
pip install requests

"""


response = requests.get("https://www.python.org")
print(f"The status code is {response.status_code}")  # Output: 200 (if successful)


"""Practice Exercises
Problem 1: Built-in Modules
Write a program that:

Generates a random number between 1 and 100.
Prints the square root of that number using the math module.
"""

random_num = random.randint(1, 100)
square_root_round = round(sqrt(random_num), 3)
print(f"Square root of random number rounded {square_root_round}")
square_root_floor = math.floor(sqrt(random_num))
print(f"Square root of random number rounded to floor {square_root_floor}")
square_root_ceil = math.ceil(sqrt(random_num))
print(f"Square root of random number rounded to ceil {square_root_ceil}")

"""Problem 2: Custom Module
Create a module math_operations.py with the following:

A function add(a, b) that returns the sum of two numbers.
A function multiply(a, b) that returns their product.
Write another script to import and use these functions."""

add_result = math_operations.add(5, 15)
print(add_result)
multiply_result = math_operations.multiply(4, 24)
print(multiply_result)


"""Problem 3: External Module
Install the requests module and write a program that fetches the HTML content of https://example.com and prints the first 100 characters."""

# Fetch the HTML content of the webpage

response = requests.get("https://example.com")

# Check if the request was successful
if response.status_code == 200:
    print(response.text[0:100])  # Print the first 100 chars of the HTML content
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")


"""Challenge Task
Modular Calculator
Create a module calculator.py with functions for:
Addition
Subtraction
Multiplication
Division
Write a script to:
Import the calculator module.
Take user input for two numbers and an operator.
Perform the calculation using the appropriate function."""

add = calculator.add(5, 10)
print(add)
subtract = calculator.subtract(5, 10)
print(subtract)
multiply = calculator.multiply(5, 10)
print(multiply)
divide = calculator.divide(5, 10)
print(divide)
