def is_different(s):
    return len(set(s)) == len(s)


print(is_different([1, 2, 3, 4, 4]))
