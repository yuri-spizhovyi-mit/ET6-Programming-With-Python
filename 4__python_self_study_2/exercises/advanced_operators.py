"""Python Lesson: Advanced and Special Operators
Introduction
In addition to basic operators like ==, !=, >=, and arithmetic operators, Python offers a variety of advanced and special operators. These operators provide additional functionality and are useful for specific scenarios like working with sequences, bitwise operations, identity checks, and more.

1. Membership Operators: in, not in
Purpose
These operators check whether a value exists in a sequence (like a list, string, or tuple).

Syntax

value in sequence
value not in sequence

"""

# Using 'in'
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Output: True
print("grape" in fruits)  # Output: False
if "apple" in fruits:
    print("Apple in fruits")
# Using 'not in'
print("grape" not in fruits)  # Output: True

"""2. Identity Operators: is, is not
Purpose
These operators check whether two variables refer to the same object in memory.

Syntax

a is b
a is not b"""
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)  # Output: True (z is the same object as x)
print(x is y)  # Output: False (x and y have the same content but are different objects)
print(x is not y)  # Output: True

"""3. Bitwise Operators
Purpose
Bitwise operators perform operations on the binary representations of numbers."""
# Example: Bitwise AND
a = 5  # Binary: 101
b = 3  # Binary: 011
c = 8  # Binary: 1000
print(a & b)  # Output: 1 (Binary: 001)

# Example: Bitwise OR
print(a | b)  # Output: 7 (Binary: 111)
print(a | c)  # Output: 13 (Binary: 111)

# Example: Bitwise XOR
print(a ^ b)  # Output: 6 (Binary: 110)

# Example: Bitwise NOT
print(~a)  # Output: -6 (Two's complement representation)

# Example: Left Shift
print(a << 1)  # Output: 10 (Binary: 1010)

# Example: Right Shift
print(a >> 1)  # Output: 2 (Binary: 10)

"""
Python Lesson: Advanced and Special Operators
Introduction
In addition to basic operators like ==, !=, >=, and arithmetic operators, Python offers a variety of advanced and special operators. These operators provide additional functionality and are useful for specific scenarios like working with sequences, bitwise operations, identity checks, and more.

1. Membership Operators: in, not in
Purpose
These operators check whether a value exists in a sequence (like a list, string, or tuple).

Syntax
python
Copy code
value in sequence
value not in sequence
Examples
python
Copy code
# Using 'in'
fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)   # Output: True
print('grape' in fruits)   # Output: False

# Using 'not in'
print('grape' not in fruits)  # Output: True
2. Identity Operators: is, is not
Purpose
These operators check whether two variables refer to the same object in memory.

Syntax
python
Copy code
a is b
a is not b
Examples
python
Copy code
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)       # Output: True (z is the same object as x)
print(x is y)       # Output: False (x and y have the same content but are different objects)
print(x is not y)   # Output: True
3. Bitwise Operators
Purpose
Bitwise operators perform operations on the binary representations of numbers.

Operator	Description
&	Bitwise AND
`	`
^	Bitwise XOR (Exclusive OR)
~	Bitwise NOT
<<	Bitwise Left Shift
>>	Bitwise Right Shift
Examples
python
Copy code
# Example: Bitwise AND
a = 5       # Binary: 101
b = 3       # Binary: 011
print(a & b)  # Output: 1 (Binary: 001)

# Example: Bitwise OR
print(a | b)  # Output: 7 (Binary: 111)

# Example: Bitwise XOR
print(a ^ b)  # Output: 6 (Binary: 110)

# Example: Bitwise NOT
print(~a)     # Output: -6 (Two's complement representation)

# Example: Left Shift
print(a << 1) # Output: 10 (Binary: 1010)

# Example: Right Shift
print(a >> 1) # Output: 2 (Binary: 10)
4. Assignment Operators
Purpose
Assignment operators perform operations and assign the result to the variable.

Operator	Example	Equivalent To
+=	a += b	a = a + b
-=	a -= b	a = a - b
*=	a *= b	a = a * b
/=	a /= b	a = a / b
//=	a //= b	a = a // b
%=	a %= b	a = a % b
**=	a **= b	a = a ** b
&=	a &= b	a = a & b
`	=`	`a
^=	a ^= b	a = a ^ b
<<=	a <<= b	a = a << b
>>=	a >>= b	a = a >> b
Example"""
x = 5
x += 3  # Same as x = x + 3
print(x)  # Output: 8

x *= 2  # Same as x = x * 2
print(x)  # Output: 16

"""5. Ternary Operator: Conditional Expressions
Purpose
The ternary operator provides a shorthand way to write conditional expressions.

Syntax
value_if_true if condition else value_if_false

"""
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

temperature = 25
show = "Hot" if temperature >= 25 else "Cold"
print(show)

"""6. Operator Overloading
Purpose
In Python, operators like +, -, and * can be overloaded to work with custom objects by defining special methods in a class.

Example"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Calls __add__
print(p3)  # Output: (4, 6)


"""Practice Exercises
Problem 1: Membership Operators
Write a program that checks if the word "Python" exists in a list of programming languages.

Problem 2: Identity Operators
Write a program to verify if two variables refer to the same object in memory.

Problem 3: Bitwise Operations
Calculate the result of:

6 & 3
6 | 3
6 << 1
Problem 4: Ternary Operator
Write a program that assigns a value "Even" or "Odd" to a variable based on whether a number is even or odd.

"""

pl_list = ["Python", "Java", "C++", "Go", "JS"]
if "Python" in pl_list:
    print("Python exists in a list of programming languages")
if "Lisp" not in pl_list:
    print("Lisp does not exist in the list of PL")

object_a = [1, 2, 3]
object_b = [1, 2, 3]
object_c = object_a


def verify_objects(a, b):
    if a is b:
        print("Two variables refer to the same object in memory")
    else:
        print("Two variables do not refer to the same object in memory")


verify_objects(object_a, object_b)
verify_objects(object_a, object_c)

print(6 & 3)
print(6 | 3)
print(6 << 3)


def even_odd(n):
    result = "Number is even" if n % 2 == 0 else "Number is odd"
    return result


print(even_odd(2))
print(even_odd(3))

"""Challenge Task
Custom Operator Overloading
Define a class Vector that supports addition (+) and scalar multiplication (*) using operator overloading.

Example:

"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overloading the + operator for vector addition
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        # Overloading the * operator for scalar multiplication
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        # Represent the vector in a readable format
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Output: Vector(4, 6)
print(v1 * 3)  # Output: Vector(3, 6)
