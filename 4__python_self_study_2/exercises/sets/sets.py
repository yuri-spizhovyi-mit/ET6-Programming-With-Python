"""
Lesson: Introduction to Sets in Python

1. What is a Set?
* A set is an unordered collection of unique items.
* Sets are mutable, meaning you can add or remove items.
* Sets do not allow duplicate elements.
2. Key Properties of Sets
* Unordered: Items in a set are not stored in any particular order.
* Unique: Duplicate elements are not allowed in a set.
* Mutable: You can add or remove elements from a set.
3. Creating a Set
You can create a set using:

* Curly braces {}.
* The set() constructor.
Example:
"""

Z = {1, 2}
X = {1, 2, 3}
print("Difference Z-X", Z - X)
print("Z&X", Z & X)
print("Difference Z-X", Z - X)
Z.add(3)
print(Z)


# Using curly braces
my_set = {1, 2, 3, 4}
print(my_set)

# Using set() constructor
another_set = set([1, 2, 2, 3, 4, 4])
print(another_set)  # Duplicate elements will be removed

one_more_set = {3, 2, 1}
print(one_more_set)
two_more_set = set([8, 9, 10])
print(two_more_set)

"""4. Adding and Removing Elements

* Add: Use add() to add one element.
* Update: Use update() to add multiple elements.
* Remove: Use remove() or discard() to delete an element.

Example:
"""
# Create a set
fruits = {"apple", "banana", "cherry"}

# Adding elements
fruits.add("orange")
print("Fruits: ", fruits)

# Updating with multiple elements
fruits.update(["grape", "mango"])
print("Updated fruits", fruits)

# Removing elements
fruits.remove("banana")  # Throws an error if the item does not exist
print("Removed banana", fruits)

fruits.discard("mango")  # Does NOT throw an error if the item is missing
print("Removed mango", fruits)

"""5. Set Operations
Python provides powerful operations for sets such as union, intersection, difference, and symmetric difference.

Operation	Method	Symbol	Description
Union	set.union()	`	`
Intersection	set.intersection()	&	Finds common elements.
Difference	set.difference()	-	Elements in A but not in B.
Symmetric Difference	set.symmetric_difference()	^	Elements in A or B, not both.
"""
# Example: Set Operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("Difference A-B:", A - B)
print("Difference B-A:", B - A)

# Symmetric Difference
print("Symmetric Difference:", A ^ B)

union_set = A | B
print(union_set)
intersection_set = A & B
print("Intersection set", intersection_set)
diff_a_b = A - B
print("Difference A - B", diff_a_b)
diff_b_a = B - A
print("Difference B - A", diff_b_a)
symmetric_diff = A ^ B
print("Symmetric Difference", symmetric_diff)

"""6. Checking Membership
You can use the in keyword to check if an item exists in a set.

Example:
  """
numbers = {1, 2, 3, 4, 5}

if 3 in numbers:
    print("3 is in the set")

if 6 not in numbers:
    print("6 is not in the set")

"""7. Iterating Through a Set
Use a for loop to iterate through elements of a set.

Example:
  """
colors = {"red", "green", "blue"}

for color in colors:
    print(color)
