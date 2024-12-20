"""
Created on 2024-12-08

@author: Yurii Spizhovi
"""


def mystery_5(a: list, b=None) -> list:
    """Function rearranges elements of the input list a in ascending order and appends
    them to the provided list b. If list b is not provided, the function creates it.

    Args:
        a (list): a list of elements
        b (list, optional): a list of elements. Defaults to None.

    Returns:
        list: a sorted list a appended to the list b

    Raises:
        TypeError: If elements in the list are of incompatible types.

    >>> mystery_5([])
    []

    >>> mystery_5([3, 2, 1])
    [1, 2, 3]

    >>> mystery_5([3, 2, -1])
    [-1, 2, 3]

    >>> mystery_5([5, 4], [3, 2, 1])
    [3, 2, 1, 4, 5]

    >>> mystery_5(['a', 'b', 'c'])
    ['a', 'b', 'c']

    >>> mystery_5(['!', '@', '#', 'a', '1', 'A'])
    ['!', '#', '1', '@', 'A', 'a']

    >>> mystery_5(['Z', 'a', 'A', '!', 5, 2])
    Traceback (most recent call last):
    ...
    TypeError: All elements in the list must be of compatible types.

    >>> mystery_5([3, '*', '&'], ['$', '^'])
    Traceback (most recent call last):
    ...
    TypeError: All elements in the list must be of compatible types.

    >>> mystery_5(['!'])
    ['!']

    >>> mystery_5(['abc', 'xyz', '123', '!@#'])
    ['!@#', '123', 'abc', 'xyz']

    >>> mystery_5([], ['!@#', 'xyz'])
    ['!@#', 'xyz']

    >>> mystery_5(['-3', '-1', '0', 3])
    Traceback (most recent call last):
    ...
    TypeError: All elements in the list must be of compatible types.

    >>> mystery_5([10**6, -10**6, 0])
    [-1000000, 0, 1000000]

    >>> mystery_5([], None)
    []

    >>> mystery_5([3, 2, 1], None)
    [1, 2, 3]
    """
    if b is None:
        b = []

    # If both lists are empty, return immediately
    if not a and not b:
        return b

    # Determine type to check against
    type_to_check = type(a[0]) if a else type(b[0])

    # Validate that all elements are of the same type
    if not all(isinstance(x, type_to_check) for x in a + b):
        raise TypeError("All elements in the list must be of compatible types.")

    # If `a` is empty, sort and return `b`
    if not a:
        return sorted(b)

    # Sort `a` and append its elements to `b`
    a_sorted = sorted(a)
    b.extend(a_sorted)

    return b
