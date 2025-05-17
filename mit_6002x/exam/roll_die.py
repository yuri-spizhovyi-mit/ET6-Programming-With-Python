import random


def roll_die():
    """Return random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])


def roll_n(n):
    result = ""
    for i in range(n):
        result += str(roll_die())
    return result
