def assign(k, v):
    """k (the key) and v (the value), immutable objects"""

    keys = [3, 4]
    values = ["a", "b"]
    # FILL THIS IN
    if k not in keys:
        keys.append(k)
        values.append(v)
    else:
        ind = keys.index(k)
        values.pop(ind)
        values.insert(ind, v)
    return (keys, values)


print(assign(4, "c"))
