"""Python Lesson: Arguments - Positional and Keyword
Introduction
When calling functions in Python, arguments can be passed in two primary ways:

Positional Arguments: Values are assigned to parameters based on their position.
Keyword Arguments: Values are assigned to parameters by explicitly naming the parameter.
Understanding these argument types helps in writing flexible and readable functions.

1. Positional Arguments
Definition
Positional arguments are passed to a function in the order in which the parameters are defined.

Syntax
def function_name(param1, param2):
    ...
    
function_name(arg1, arg2)

"""


def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet("Alice", 25)  # Positional arguments: "Alice" -> name, 25 -> age

"""Key Points
Order matters! If you swap the arguments, the function may behave incorrectly.
All required positional arguments must be provided in a function call unless they have default values.
2. Keyword Arguments
Definition
Keyword arguments are passed to a function by explicitly specifying the parameter name, regardless of the parameter’s position.

Syntax
def function_name(param1, param2):
    ...

function_name(param1=value1, param2=value2)

"""


def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet(age=25, name="Alice")  # Keyword arguments
"""Key Points
The order of keyword arguments doesn’t matter.
Keyword arguments improve readability, especially when functions have many parameters.
3. Combining Positional and Keyword Arguments
Rules
Positional arguments must appear before keyword arguments in a function call.
You cannot provide the same parameter twice using both positional and keyword arguments.
Example"""


def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")


# Mixing positional and keyword arguments
greet("Alice", age=25)  # Valid

# greet(name="Alice", 25)  # Invalid: Positional after keyword
# greet("Alice", name="Alice")  # Invalid: Multiple values for the same argument
"""4. Default Values with Keyword Arguments
Definition
Parameters can have default values, making them optional in function calls. These parameters can be omitted or provided as keyword arguments.

Example"""


def greet(name="Guest", age=18):
    print(f"Hello, {name}! You are {age} years old.")


greet()  # Both defaults are used
greet("Alice")  # Only `age` uses default
greet(age=25, name="Bob")  # Override both defaults

"""5. Arbitrary Positional (*args) and Keyword Arguments (**kwargs)
For functions that accept an unknown number of arguments:

Use *args to collect additional positional arguments.
Use **kwargs to collect additional keyword arguments.
Example"""


def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


display_info(1, 2, 3, name="Alice", age=25)

"""Practice Exercises
Problem 1: Positional Arguments
Write a function calculate_area that takes length and width as positional arguments and returns the area of a rectangle.

Problem 2: Keyword Arguments
Write a function introduce that takes name (default "Unknown") and age (default 0) as keyword arguments and prints a message.

Problem 3: Combining Positional and Keyword Arguments
Write a function book_ticket that takes event (positional), seat (keyword with default "General"), and price (keyword with default 0). 
Call the function with different combinations of arguments.

"""


# Problem 1
def calculate_area(length: int, width: int) -> int:
    print(f"The area of the figure is {length * width}")


calculate_area(10, 5)

# Problem 2


def name_age(name: str, age: int) -> str:
    print(f"The name of the person is {name} and name is {age}")


name_age(name="John", age=30)

# Problem 3


def book_ticket(seat, price) -> str:
    print(f"The seat type is {seat} and price is {price}")


book_ticket("General", price=100)

"""Challenge Task
Custom Function with Mixed Arguments
Create a function order_food that demonstrates:

Positional arguments for food and quantity.
A default keyword argument for drink (default "Water").
Additional items as *args.
Optional special instructions as **kwargs.
Example Call:"""


def order_food(food, quantity, *args, drink="Water", **kwargs):
    print(
        f"The order is {food}, the quantity is {quantity}. Drink is {drink} other stuff is {args} and {kwargs}"
    )


order_food("Pizza", 2, "Fries", "Salad", drink="Soda", tip=5, notes="Extra cheese")
