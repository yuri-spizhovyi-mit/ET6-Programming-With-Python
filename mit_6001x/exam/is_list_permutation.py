def is_list_permutation(L1, L2):
    """
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type

    Input:
    L1: list of integers and/or strings
    L2: list of integers and/or strings

    Returns: False if L1 is not a permutation of L2
    if True: tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type

    """
    # Your code here
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    l1_dict = {}
    l2_dict = {}
    for i in range(len(L1)):
        l1_dict[L1[i]] = l1_dict.get(L1[i], 0) + 1
    for i in range(len(L2)):
        l2_dict[L2[i]] = l2_dict.get(L2[i], 0) + 1
    if l1_dict == l2_dict:
        value_max = 0
        for key, value in l1_dict.items():
            if value > value_max:
                key_max = key
                value_max = value
        return (key_max, value_max, type(key_max))
    else:
        return False


# L1 = [1, "b", 1, "c", "c", 1]
# L2 = ["c", 1, "b", 1, 1, "c"]
L1 = []
L2 = []
print(is_list_permutation(L1, L2))
