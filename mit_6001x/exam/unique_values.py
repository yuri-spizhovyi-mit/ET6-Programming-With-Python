def uniqueValues(aDict):
    """
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    """
    amount_of_value = {}
    for key in aDict:
        val = aDict[key]
        if val in amount_of_value:
            amount_of_value[val] += 1
        else:
            amount_of_value[val] = 1
    result = []
    for key in aDict:
        if amount_of_value[aDict[key]] == 1:
            result.append(key)
    return sorted(result)


# aDict = {6: 0, 7: 0, 10: 0}
aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0, 2: 654, 345: 2345}
print(uniqueValues(aDict))
