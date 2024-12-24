"""Python Lesson: Scope Modifiers (nonlocal and global)
Introduction
In Python, variables have different scopes depending on where they are defined:

Local Scope: Inside a function or block.
Global Scope: Outside of all functions.
Enclosing Scope: Inside nested functions.
Built-in Scope: Predefined by Python (e.g., len, print).
Scope modifiers like nonlocal and global allow us to modify variables in specific scopes.

1. global Modifier
Definition
The global keyword allows a variable defined outside a function (global scope) to be modified inside the function.

Syntax
python
Copy code
global var_name
Use Case
When you need to modify a global variable inside a function.

Example
Key Points
Without global, assigning to a variable inside a function creates a new local variable.
Use global sparingly; modifying global variables can make your code harder to understand.
"""

x = 10  # Global variable


def modify_global():
    global x
    x += 5  # Modify the global variable
    print(f"Inside function: x = {x}")


modify_global()
print(f"Outside function: x = {x}")

"""2. nonlocal Modifier
Definition
The nonlocal keyword allows a variable in an enclosing scope (not global) to be modified inside a nested function.

Syntax
python
Copy code
nonlocal var_name
Use Case
When you need to modify a variable in the enclosing (outer) function scope inside a nested function.

Example"""


def outer_function():
    x = 10  # Enclosing scope variable

    def inner_function():
        nonlocal x
        x += 5  # Modify the enclosing scope variable
        print(f"Inside inner function: x = {x}")

    inner_function()
    print(f"Inside outer function: x = {x}")


outer_function()

"""Key Points
nonlocal only works in nested functions and modifies variables in the nearest enclosing scope.
Without nonlocal, assigning to a variable inside a nested function creates a new local variable.
3. Difference Between global and nonlocal
Feature	global	nonlocal
Modifies	Global variables	Variables in the enclosing scope
Works Inside	Any function	Nested functions only
Creates	No new variable, modifies global	No new variable, modifies enclosing"""

"""Practice Exercises
Problem 1: Using global
Write a program that uses a global counter variable. Increment the counter by 1 every time a function is called.

Problem 2: Using nonlocal
Write a program with a nested function that modifies a variable in the enclosing function’s scope.

Problem 3: Combining global and nonlocal
Write a program where:

A global variable tracks the total score.
A nested function modifies the score of an enclosing function, which contributes to the total score.
"""

# Problem 1: Using global
counter_var = 0


def counter():
    global counter_var
    counter_var += 1
    print(f"Local {counter_var}")


counter()

# Problem 2: Using nonlocal


def outer():
    x = 5

    def inner():
        nonlocal x
        x += 10
        print(f"Inner var {x}")

    inner()
    print(f"Outer {x}")


outer()

# Problem 3: Combining global and nonlocal

total = 0


def out():
    global total
    score = 0

    def inner():
        nonlocal score
        score += 1
        print(f"Score is {score}")

    inner()
    total += score


out()
print(f"Total score is {total}")

"""Counter with Nonlocal and Global
Create a program where:

A global variable total_calls tracks how many times a function is called.
A nested function uses nonlocal to maintain a counter for how many times the inner function is executed.
Print both counters each time the function is called.
Example Output:

mathematica

Total calls: 1, Inner function calls: 1
Total calls: 2, Inner function calls: 2"""

total_calls = 0


def outer():
    global total_calls
    total_calls += 1
    inner_calls = 0

    def inner_f():
        nonlocal inner_calls
        inner_calls += 1

    inner_f()
    inner_f()
    print(f"Total calls: {total_calls}, Inner function calls: {inner_calls}")


outer()
outer()
