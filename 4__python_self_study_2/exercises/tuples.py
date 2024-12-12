"""Python Tuples: A Short Explanation
A tuple in Python is an ordered, immutable collection of items. Unlike lists, you cannot change, add, or remove items in a tuple after it is created. Tuples are useful for storing data that shouldn't be modified.

Key Features:
Defined using parentheses () or without brackets (comma-separated).
Items in a tuple can be of any data type.
Tuples allow duplicates.
Immutable: You cannot change their elements.

  """

# Example 1: Simple tuple
fruits = ("apple", "banana", "cherry")

# Example 2: Tuple with mixed data types
person = ("Alex", 30, "Kelowna")

# Example 3: Single-item tuple (note the comma)
single = ("only one",)  # Must include a comma!

print(fruits[0])  # Output: apple
print(person[1])  # Output: 30

for fruit in fruits:
    print(fruit)
# Tuple Operations
# 1. Concatenation:
new_tuple = fruits + ("grape", "orange")
print(new_tuple)  # Output: ('apple', 'banana', 'cherry', 'grape', 'orange')
# 2 Repetition:

repeated = fruits * 2
print(repeated)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# 3 Membership Testing:
print("apple" in fruits)  # Output: True
print("kiwi" in fruits)  # Output: False

# Tuple Unpacking
# You can unpack a tuple into variables:
name, age, city = person
print(name)  # Output: Alex
print(city)  # Output: Kelowna

# Use Cases of Tuples
# 1. Storing Fixed Data:
coordinates = (49.8879, -119.4960)  # Latitude and Longitude


# 2. Returning Multiple Values from a Function:
def get_dimensions():
    return (1920, 1080)


width, height = get_dimensions()
print(width, height)  # Output: 1920 1080
# 3. As Dictionary Keys: Tuples can be used as dictionary keys because they are immutable:
location = {(49.8879, -119.4960): "Kelowna"}
print(location)

# Example: Using Tuples in Practice
# Store information about a book
book = ("1984", "George Orwell", 328)

# Access book details
title, author, pages = book
print(f"Title: {title}, Author: {author}, Pages: {pages}")

# Immutable: Can't modify, but you can create a new tuple
book = book + ("Dystopian",)  # Adding a new category
print(book)
# Examples
# 1. Adding Elements by Creating a New Tuple:
original = (1, 2, 3)
new_tuple = original + (4, 5)  # Creates a new tuple
print(new_tuple)  # Output: (1, 2, 3, 4, 5)
# 2. Deleting an Entire Tuple:
original = (1, 2, 3)
del original  # Deletes the entire tuple
# print(original)  # Error: NameError because the tuple no longer exists
# 3. Cannot Modify or Remove Elements:
original = (1, 2, 3)
# original[0] = 10  # Error: TypeError
# del original[1]  # Error: TypeError
