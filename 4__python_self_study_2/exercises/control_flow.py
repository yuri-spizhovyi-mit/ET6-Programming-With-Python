"""
Python Lesson: Control Flow
Introduction
Control flow determines the order in which a program executes instructions. Python provides several constructs for control flow, including:

Ternary Conditional Operator (_ if _ else _)
For Loops (_ for _ in _)
break Statement
continue Statement
Let’s dive into each with examples and practice exercises.

1. Ternary Conditional Operator: _ if _ else _
Definition
The ternary conditional operator is a one-line shorthand for an if-else statement. It allows conditional expressions in a concise format.

Syntax


Python Lesson: Control Flow
Introduction
Control flow determines the order in which a program executes instructions. Python provides several constructs for control flow, including:

Ternary Conditional Operator (_ if _ else _)
For Loops (_ for _ in _)
break Statement
continue Statement
Let’s dive into each with examples and practice exercises.

1. Ternary Conditional Operator: _ if _ else _
Definition
The ternary conditional operator is a one-line shorthand for an if-else statement. It allows conditional expressions in a concise format.

Syntax
python
Copy code
value_if_true if condition else value_if_false
Key Points
Avoid overcomplicating expressions to maintain readability.
Suitable for simple conditional assignments."""
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)

"""**2. For Loops: _ for _ in _
Definition
The for loop iterates over a sequence (e.g., list, tuple, string) or any iterable object.

Syntax

for variable in iterable:
    # Code to execute for each item
"""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")
"""Using range() with for
range() generates a sequence of numbers."""
for i in range(1, 5):
  print(i)
  
"""List Comprehensions
Python provides a compact syntax for creating lists with for loops."""

numbers = [x**2 for x in range(5)] # Squares of numbers 0 to 4
print(numbers)
"""3. break Statement
Definition
The break statement exits the loop immediately, regardless of the iteration condition.

Example"""
for i in range(10):
  print(i, end=" ")
  if i == 5:
    break
  
"""4. continue Statement
Definition
The continue statement skips the current iteration and moves to the next iteration of the loop.

Example"""
print("---")
for i in range(5):
  print(i)
  if i == 2:
    continue
  

"""
Practice Exercises
Problem 1: Ternary Operator
Write a program that checks if a number is even or odd using a ternary operator.

Problem 2: for Loop
Write a program that prints all numbers from 1 to 20, but stops if the number 15 is reached.

Problem 3: break
Write a program that iterates through a list of names. If the name "John" is found, stop iterating and print "John found".

Problem 4: continue
Write a program that iterates through numbers 1 to 10 but skips numbers divisible by 3.


"""
# Problem 1
number = 2
result = "Even" if number%2==0 else "Odd"
print(result)

# Problem 2

for i in range(20):
  print(i, end=" ")
  if i == 15:
    break
  

# Problem 3

names = ["Eve", "Bea", "Colin", "John", "Edward"]
for name in names:
  if name == "John":
    break
  print(name)

# Problem 4

for i in range(11):
  if i%3 == 0:
    continue
  print(i)

"""Challenge Task
Custom Loop
Create a program that:

Uses a for loop to iterate over a range of numbers from 1 to 50.
Prints "Fizz" for numbers divisible by 3, "Buzz" for numbers divisible by 5, and "FizzBuzz" for numbers divisible by both.
Skips numbers divisible by 7 using continue.
Stops the loop entirely if the number 45 is reached using break.
Expected Output:

"""
for i in range(1,50):
  if i == 45:
    break
  if i%7 == 0:
    continue
  if i%3 == 0 and i%5 == 0:
    print(f"{i} is Fizz&Buzz")
  elif i%3 == 0:
    print(f"{i} is Fizz")
  elif i%5 == 0:
    print(f"{i} is Buzz")
