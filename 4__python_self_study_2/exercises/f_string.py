from datetime import datetime
"""Python Lesson: F-Strings (f"... {expression} ...")
Introduction
Python's f-strings (formatted string literals) provide a concise and readable way to include expressions and variables inside strings. Introduced in Python 3.6, f-strings start with an f or F before the string and use curly braces {} to evaluate expressions directly within the string.

1. Basics of F-Strings
Syntax
python
Copy code
f"Text {expression}"
f or F: Indicates that the string is a formatted string literal.
{expression}: Any valid Python expression (variable, calculation, function call) enclosed in curly braces.
Example
"""
name = "Alex"
age = 30
print(f"My name is {name} and I am {age} years old.")
"""2. Using Expressions in F-Strings
F-strings allow more than just variable substitution—you can include any Python expression.

Arithmetic Operations
  """
width = 10
height = 5
print(f"The area of the rectange is {width * height}")
# Function Calls
def greet(name):
  return f"Hello {name}"

print(f"Message: {greet('Alex')}")

# Inline Conditions
temperature = 125
print(f"It's {'cold' if temperature < 20 else 'warm'} today")

"""3. Formatting with F-Strings
You can format numbers, dates, and strings within f-strings using special formatting syntax.

Aligning Text
Left-aligned: {variable:<width}
Right-aligned: {variable:>width}
Center-aligned: {variable:^width}
"""
name = "Alex"
print(f"|{name:<20}|")
print(f"|{name:>20}|")
print(f"|{name:^20}|")

"""Formatting Numbers
Decimal Places: {number:.nf} (n = number of decimal places)
Thousands Separator: {number:,}
"""
pi = 3.14159265359
large_number = 123456789
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Formatted large number: {large_number:,}")

"""Date Formatting
For advanced date formatting, use the datetime module.
"""

now = datetime.now()
print(f"Today's date: {now:%Y-%m-%d}")
print(f"Current time: {now:%H:%M:%S}")

"""4. Escaping Curly Braces
To include literal curly braces in an f-string, double them ({{ or }}).
"""
value = 10
print(f"Use double curly braces to display a value: {{value}} = {value}")

"""5. Multiline F-Strings
F-strings can span multiple lines when enclosed in triple quotes.
"""
name = "Alex"
age = 30

message = f"""
Hello {name},
You are {age} years old.add()
Have a great day!"""
print(message)

"""Practice Exercise
Problem 1: Basic F-Strings
Write a program that takes a user's name and age as input, and prints a message using an f-string:
"""
#name = input("Enter your name: ")
#age = input("Enter you age: ")
#print(f"My name is {name} and I am {age} years old")

"""Problem 2: Formatting Numbers
Display a floating-point number (e.g., 1234.5678) with:

2 decimal places
A thousands separator
"""

number = 1234.5678
print(f"2 decimal places number {number:.2f}")
print(f"A thousand separator number: {number:,}")

"""Problem 3: Dynamic Greeting
Write a program that generates a greeting based on the current time:

Before 12 PM: "Good Morning!"
12 PM to 6 PM: "Good Afternoon!"
After 6 PM: "Good Evening!"
Use f-strings and the datetime module.
"""
current_date = datetime.now()
current_hour = current_date.hour
if current_hour < 12:
  greeting = "Good Morning!"
elif 12 < current_hour < 6:
  greeting = "Good Afternoon!"
else: 
  greeting = "Good Evening!"

print(f"{greeting} The current time is {now:%I:%M:%p}")


"""Challenge Task
Dynamic Table
Create a dynamic table using f-strings to align data neatly.

Input: A list of tuples with student names and scores.
"""
students = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
print(f"{'Name':<10}{'Score':>10}")
print("-"*20)
for name, score in students:
  print(f"{name:<10}{score:>10}")
  
  # Calculate column widths
name_width = max(len(name) for name, _ in students) + 2
score_width = 6
  
  # Header
print(f"{'Name':<{name_width}}{'Score':>{score_width}}")
print("-" * (name_width + score_width))
  
  # Table Rows
for name, score in students:
  print(f"{name: <{name_width}}{score:>{score_width}}")
