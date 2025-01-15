"""
Created on 2024-12-08

@author: Yurii Spizhovyi
"""


def sum_evens_and_odds(numbers: list[int]) -> dict[str, int]:
    """
    Sum the even and odd numbers in a list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        dict[str, int]: A dictionary with two keys:
                        - "evens": The sum of even numbers in the list.
                        - "odds": The sum of odd numbers in the list.

    Raises:
        TypeError: If the input is not a list of integers.

    Examples:
        >>> sum_evens_and_odds([1, 2, 3, 4])
        {'evens': 6, 'odds': 4}

        >>> sum_evens_and_odds([])
        {'evens': 0, 'odds': 0}

        >>> sum_evens_and_odds([2, 4, 6, 8])
        {'evens': 20, 'odds': 0}

        >>> sum_evens_and_odds([-2, -3, 4, 5])
        {'evens': 2, 'odds': 2}

        >>> sum_evens_and_odds([0, 0, 0])
        {'evens': 0, 'odds': 0}

    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers.")

    evens = sum(num for num in numbers if num % 2 == 0)
    odds = sum(num for num in numbers if num % 2 != 0)

    return {"evens": evens, "odds": odds}


print(sum_evens_and_odds([1, 2, 3, 4]))
