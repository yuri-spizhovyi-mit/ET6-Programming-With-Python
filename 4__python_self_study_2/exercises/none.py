"""Python Lesson: Data Types: None
Introduction
None is a special constant in Python that represents the absence of a value or a null value. It is commonly used to signify "nothing" or "no value here." It is an immutable singleton, meaning there is only one instance of None in a Python program.

1. What is None?
None is an object of its own data type, called NoneType.
It is used to denote the absence of a value or a null value.
Common use cases:
Default return value of functions without a return statement.
Placeholder for optional or uninitialized variables.
Representing "no value" in data structures.
"""
x = None
print(x)             # Output: None
print(type(x))       # Output: <class 'NoneType'>

"""2. How None is Used
2.1. As a Default Return Value
If a function does not explicitly return a value, it returns None.
"""

def none_function():
  pass

result = none_function()
print(result)
"""2.2. As a Placeholder
None is often used as a placeholder for variables that will be assigned a value later."""
data = None
print(data)          # Output: None

# Assign a value later
data = "Hello, World!"
print(data)          # Output: Hello, World!

"""2.3. Representing "No Value" in Data Structures
None is used in collections (e.g., lists, dictionaries) to signify missing or undefined values.
"""
my_list = [1, None, 3, None]
print(my_list)       # Output: [1, None, 3, None]

my_dict = {"key1": None, "key2": "value"}
print(my_dict)       # Output: {'key1': None, 'key2': 'value'}

"""2.4. Comparing to None
To check if a variable is None, use the is operator instead of ==. This ensures you are checking identity rather than equality."""
x = None

# Correct way
if x is None:
    print("x is None")

# Incorrect way (not recommended)
if x == None:  # This works but is less precise
    print("x is None")

"""3. None vs Other Values
None is not the same as:
0: Zero is a number, while None is a null object.
False: False is a Boolean value, while None means no value.
"": An empty string is still a value, while None represents the absence of a value.
Examples"""
print(None == 0)      # Output: False
print(None == False)  # Output: False
print(None == "")     # Output: False

"""4. Functions that Return None
Some built-in Python functions return None when they perform an action but do not explicitly return a value.

Example: list.append()"""
my_list = [1, 2, 3]
result = my_list.append(4)  # Appends 4 to the list
print(result)               # Output: None
print(my_list)              # Output: [1, 2, 3, 4]

"""5. Common Mistakes with None
Confusing None with Falsy Values

None is falsy, but it is different from False, 0, or an empty string.
Always use is None for comparisons.
Using None in Arithmetic Operations

Attempting to perform arithmetic with None will raise an error."""
try:
  x = None
  print(x + 1)  # Raises TypeError
except TypeError:
  print("Attempting to perform arithmetic with None will raise an error.")

"""Practice Exercise
Problem 1: Placeholder
Create a variable status with an initial value of None. Later, update it based on user input.

"""
# Initial status
status = None

# Update based on input
# Input: "complete"
#status = input("Enter a status e.g. 'complete', 'in progress' etc.: ")
# Output: Status is complete
#print(f"Status is {status}")

"""Problem 2: Check for None
Write a function that takes a list and prints the indices of all elements that are None."""

some_list = ['asdf', 1, None, None]

def none_function(n:list[str, int, None]) -> str:
  """Function for printing an index of None value element in a list"""
  for key, value in enumerate(n):
    if value is None:
      print(f"Element at index {key} is None")
  
none_function(some_list)

"""Challenge Task
Custom Function with None Defaults
Create a function divide that divides two numbers. If the divisor is None, return "Divisor is missing". 
If the divisor is zero, return "Cannot divide by zero". Otherwise, return the result of the division."""

def divide(dividend, divisor=None):
    if divisor is None:
      return "Dividend is missing"
    if divisor == 0:
      return "Cannot divide by zero"
    return dividend / divisor

print(divide(6, 3))
print(divide(6, None))
print(divide(6, 0))
# Example calls:
# divide(10, 2) -> 5
# divide(10, 0) -> "Cannot divide by zero"
# divide(10) -> "Divisor is missing"

"""Summary
None represents the absence of a value.
Use is to check for None.
Commonly used as a placeholder, default return value, or to signify missing data.
Avoid arithmetic or logical operations with None.
Feel free to try the exercises or ask for clarifications! 😊
"""
