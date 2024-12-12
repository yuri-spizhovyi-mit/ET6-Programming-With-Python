"""A dictionary in Python is a collection of key-value pairs. Each key is unique and acts as an identifier, while the value can be any data type. Dictionaries are mutable, meaning you can change them after creation.

Key Features:
Defined using {}.
Keys must be immutable types (e.g., strings, numbers, tuples).
Values can be any type.
Access values by their key."""

# Example 1: Simple dictionary
person = {"name": "Alex", "age": 30, "city": "Kelowna"}

print(person["name"])  # Output: Alex
print(person["age"])  # Output: 30

# Adding a new key-value pair

person["profession"] = "Developer"
print(person)

# Updating an existing key
person["age"] = 31
print(person)

# Removing items using del
del person["city"]
print(person)

# Using pop (returns the value)
age = person.pop("age")
print(age)  # Output 31
print(person)  # City removed

# Looping through a dictionary
# Keys only:
for key in person:
    print(key)

# Values only:
for value in person:
    print(value)

# Keys and values:
for key, value in person.items():
    print(f"{key}:{value}")

# Checking existence of a key
if "name" in person:
    print("Name exists in the dictionary")


# A Simple use case

# Storing student grades

grades = {"Alice": 85, "Bob": 92, "Charlie": 82}

# Accessing grades

print(grades["Alice"])  # Output: 85

# Adding a new students
grades["Diana"] = 88

# Updating a grade
grades["Alice"] = 90

# Removing a student
del grades["Charlie"]

# Looping through the grades
for student, grade in grades.items():
    print(f"{student}: {grade}")
