from collections import Counter


def most_frequent_char(s: str) -> str:
    if not s:
        return None

    count = Counter(s)
    return max(count, key=count.get)


print(most_frequent_char("hello"))  # "l"
print(most_frequent_char("aabbbcccc"))  # "c"
print(most_frequent_char("xyzxyzxyz"))  # "x", "y", or "z" (any of them)
