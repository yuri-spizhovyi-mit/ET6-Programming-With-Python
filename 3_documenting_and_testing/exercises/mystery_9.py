"""Created on 2024-12-08

@author: Yurii Spizhovyi
"""


def mystery_9(a: list[int]) -> list[int]:
    """Function for sorting a list of numbers

    Parameters:
    a: list[int] a list of numbers

    Returns: list[int] a list of sorted in ascending order numbers

    >>> mystery_9([])
    []

    >>> mystery_9([100, 0, -10])
    [-10, 0, 100]


    """
    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a


mystery_9([5, 2, 6, 4])
