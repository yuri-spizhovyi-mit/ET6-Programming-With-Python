def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float("nan")

    lengths = [len(s) for s in L]
    mean = sum(lengths) / len(L)
    return (sum((l - mean) ** 2 for l in lengths) / len(L)) ** 0.5


# L = ['a', 'z', 'p']
L = ["apples", "oranges", "kiwis", "pineapples"]
stdDevOfLengths(L)
