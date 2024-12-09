"""
Created on 2024-12-08

@author: Yurii Spizhovi
"""


def mystery_5(a: int, b=None) -> list[int]:
    """Function rearranges elements of the input list a in ascending order and appends
    them to the provided list b. If  list b is not provided, the function creates it.

    Args:
        a (int): a list of elements
        b (_type_, optional): a list of elements. Defaults to None.

    Returns:
        list[int]: a sorted list a appended to the list b
        
        
    >>> mystery_5([])
    []
    
    >>> mystery_5([3, 2, 1])
    [1, 2, 3]
    
    >>> mystery_5([3, 2, -1])
    [-1, 2, 3]
    
    >>> mystery_5([5, 4], [3, 2, 1])
    [3, 2, 1, 4, 5]
    >>>
    """
    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b

mystery_5([3,4])
