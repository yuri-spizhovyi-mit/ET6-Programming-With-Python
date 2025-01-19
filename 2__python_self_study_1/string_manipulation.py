"""Lesson on String Manipulation in Python
Strings in Python are a sequence of characters. Python provides powerful tools to manipulate and work with strings. Here's a breakdown of the most commonly used string manipulation techniques:

"""
"""1. Indexed Access
Strings are indexed, meaning each character in a string has a position (index), starting from 0.
"""
my_string = "Python"
print(my_string[0])  # Should print "P"
print(my_string[1])  # Should print "y"

# Slicing

"""2. Slicing
You can extract a portion of a string using slicing. The syntax is string[start:end:step].

start: The starting index (inclusive).
end: The ending index (exclusive).
step: Optional, specifies the step size (default is 1).
"""
print(my_string[0:2])  # Should print "Py"
print(my_string[2:5])  # Should print "tho"
print(my_string[2:])  # Should print "thon"
print(my_string[:2])  # Should print "Py"
print(my_string[:])  # Should print "Python"
print(my_string[::-1])  # Reverses the string -> 'nohtyP'

"""
3. Length of a String
Use the len() function to find the number of characters in a string.

"""
print(len(my_string))  # Should print 6

"""4. String Methods
a) .replace()
Replaces occurrences of a substring with another substring."""

text = "Hello, World!"
print(text.replace("World", "Python"))  # Should print "Hello, Python!"

"""
b) .upper() and .lower()
Converts the string to uppercase or lowercase.
"""

text = "Hello World!"
print(text.upper())  # Should print "HELLO WORLD!"
print(text.lower())  # Should print "hello world!"
print(text.capitalize())  # Should print "Hello world!"

"""
c) .strip()
Removes leading and trailing whitespace (or specific characters if provided).
"""

text = "   Hello, World!   "
print(text.strip())  # Should print "Hello, World!"

"""
5. Membership Check (in)
Check if a substring exists within another string using the in keyword.
"""
text = "Python is fun"
print("Python" in text)  # Should print True
print("Java" in text)  # Should print False
print("P" in text)  # Should print True

"""Example: Combining Methods
"""

message = "  Welcome to Python programming  "
# Clean up the string, convert to lowercase, and check for a substring
clean_message = message.strip().lower().replace("python", "Java")
print(clean_message)  # Should print "welcome to Java programming"
print("Java" in clean_message)  # Should print False

"""Task 1: Reverse a String
Write a program to reverse the string "Learning".
"""

text_to_reverse = "Learning"
reversed_text = text_to_reverse[::-1]
print(reversed_text)  # Should print "gninraeL"

"""Task 2: Case Conversion
Convert "hello world" to "HELLO WORLD" and "GOODBYE" to "goodbye"."""

text_1 = "hello world"
text_2 = "GOODBYE"

converted_text_1 = text_1.upper()
converted_text_2 = text_2.lower()
print(converted_text_1)  # Should print "HELLO WORLD"
print(converted_text_2)  # Should print "goodbye"
