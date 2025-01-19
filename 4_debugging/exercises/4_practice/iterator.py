"""
Define a function that iterates over a list of numbers,
multiplies each number by one less than its index position
and returns the total sum of those products
"""
from typing import List

def sum_of_products(numbers: List[int]) -> int:
   return sum(x * (i - 1) for i, x in enumerate(numbers))

print(sum_of_products([1, 2, 3, 4, 5]))
