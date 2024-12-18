"""
Python Lesson: Iteration with iter(), next(), and enumerate()
Introduction
Iteration is a fundamental concept in programming that involves looping through data. Python provides several built-in tools for iteration, including iter(), next(), and enumerate(). These functions are especially useful for working with iterators and iterable objects.

1. iter() Function
Definition
The iter() function is used to create an iterator from an iterable object (e.g., a list, string, or tuple).

Key Concepts
An iterable is any object that can return its elements one at a time.
An iterator is an object with two main methods:
__iter__() returns the iterator itself.
__next__() retrieves the next value from the iterator.


2. next() Function
Definition
The next() function retrieves the next item from an iterator. If there are no items left, it raises a StopIteration exception.

next(iterator, default_value)
The optional default_value is returned if the iterator is exhausted instead of raising StopIteration.

3. enumerate() Function
Definition
The enumerate() function adds a counter to an iterable, returning an enumerate object. This is particularly helpful when you need both the index and the value during iteration.

Syntax
"""
# Syntax

# iterator = iter(iterable)
my_list = [1, 2, 3]
iterator = iter(my_list)
print(iterator)
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3


fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
    
numbers = [5, 10, 15, 20]
# Use iter() and next() to iterate through numbers
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


names = ['Alice', 'Bob', 'Charlie']
# Use enumerate() to solve this
for index, name in enumerate(names, start=1):
  print(index, name)
