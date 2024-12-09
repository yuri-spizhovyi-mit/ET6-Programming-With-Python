"""
Created on 2024-12-08

@author: Yurii Spizhovyi
"""


def mystery_6(a: int, b: int) -> list[int]:
    """The function creates a list with `a` elements, where the first element is `b`,
    and each subsequent element increases by 1. If `a` is 0, the function returns an empty list.
    
    Parameters: 
    a: int greater or equals 0
    b: int
    
    Returns -> list[int] with the first element b and every next element is greater by 1
    
    >>> mystery_6(2, 10)
    [10, 11]
    
    >>> mystery_6(0, 10)    
    []
    
    >>> mystery_6(3, -1)
    [-1, 0, 1]
"""
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c

mystery_6(2, 10)
