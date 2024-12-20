"""Python Lesson: Parameters in Functions
Introduction
Function parameters in Python allow us to pass data into functions to customize their behavior. Python provides powerful ways to define and use parameters, including:

Default values
Variable-length arguments (*args and **kwargs)
Keyword-only parameters
Positional-only parameters
1. Default Values
Purpose
Default values allow you to specify a default value for a parameter. If no argument is passed for that parameter, the default value is used.

Syntax

def function_name(param=default_value):
    ...
"""


def greet(name="Guest"):
    print(f"Hello {name}!")


greet()
greet("Alice")


def add(a, b=1):
    return a + b


print(add(1))
print(add(1, 2))

"""Key Points
Default values must be defined at the end of the parameter list.
Avoid using mutable objects (e.g., lists, dictionaries) as default values, as this can lead to unexpected behavior.
2. Variable-Length Arguments: *args
Purpose
*args is used to pass a variable number of positional arguments to a function.

Key Points
*args collects arguments into a tuple.
Useful when the number of arguments is unknown.

Syntax

def function_name(*args):
    ...
"""


def add_numbers(*args):
    return sum(args)


print(add_numbers(1, 2, 3))
print(add_numbers(4, 6))

"""
3. Keyword Arguments: **kwargs
Purpose
**kwargs is used to pass a variable number of keyword arguments to a function.

Key Points
**kwargs collects arguments into a dictionary.
Useful for handling optional parameters.


Syntax
def function_name(**kwargs):
    ...
"""


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=30, city="New York")


"""4. Keyword-Only Parameters
Purpose
Keyword-only parameters can only be provided as keyword arguments and must follow a * in the function signature.

Key Points
Enforcing keyword-only parameters improves code readability and reduces errors.

Syntax
python

def function_name(*, param1, param2):
    ..."""


def greet(*, name="Guest"):
    print(f"Hello, {name}!")


greet(name="Alice")
# greet("Alice")      # Raises TypeError

"""5. Positional-Only Parameters
Purpose
Positional-only parameters can only be provided as positional arguments and must precede a / in the function signature.

Key Points
Introduced in Python 3.8.
Useful for parameters that should not be passed as keywords (e.g., in mathematical or API functions).

Syntax

def function_name(param1, param2, /, param3):
    ..."""


def divide(a, b, /):
    return a / b


print(divide(10, 2))  # Output: 5.0
# print(divide(a=10, b=2))  # Raises TypeError

"""Combining Different Parameter Types
Python functions allow a combination of all these parameter types. The order in the function signature should be:

Positional-only parameters (/)
Positional or keyword parameters
Default parameters
*args
Keyword-only parameters (*)
**kwargs
Example"""


def example_func(a, b=10, /, *args, c, d="Default", **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"c: {c}, d: {d}")
    print(f"kwargs: {kwargs}")


example_func(1, 2, 3, 4, c=5, d="Custom", e=6, f=7)

"""Practice Exercises
Problem 1: Default Parameters
Write a function that takes two arguments, name (default "Guest") and greeting (default "Hello"), and prints a greeting message.

Problem 2: *args
Write a function that calculates the product of all numbers passed as arguments.

Problem 3: **kwargs
Write a function that takes any number of keyword arguments and prints only the arguments where the value is greater than 10.

Problem 4: Keyword-Only Parameters
Write a function that requires a keyword argument city, with a default value "Unknown".

Problem 5: Positional-Only Parameters
Write a function that takes two positional-only parameters and returns their sum.

"""


# Problem 1
def print_greeting(name="Guest", greeting="Hello"):
    print(f"{greeting}, {name}!")


print_greeting()
print_greeting("John", "Hey")


# Problem 2
def product(*args):
    result = 1
    for item in args:
        result *= item
    return result


print(product(1, 2, 3, 4))

# Problem 3: **kwargs


def ten_more(**kwargs):
    for _, value in kwargs.items():
        if value > 10:
            print(f"Value {value} is more then 10")


ten_more(first=5, second=10, third=20)

# Problem 4: Keyword-Only Parameters


def city(*, city="Unknown"):
    print(f"West {city}")


city(city="Kelowna")

# Problem 5: Positional-Only Parameters


def sum(a, b, /):
    return a + b


print(sum(3, 5))

"""Challenge Task
Custom Function with All Parameter Types
Create a function custom_function that demonstrates:

Positional-only parameters
Default values
*args
Keyword-only parameters
**kwargs
Call it with a mix of positional, keyword, and additional arguments."""


def custom_function(a, b, /, *args, c="Default", city="Unknown", **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"c: {c}")
    print(f"city: {city}")
    print(f"kwargs: {kwargs}")


# Correct Function Call
custom_function(1, 2, 4, 5, c="Custom", city="Vancouver", e=6, f=7)
