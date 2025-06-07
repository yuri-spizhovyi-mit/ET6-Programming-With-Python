from collections import Counter


def first_unique_char(s: str) -> int:
    count = Counter(s)

    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i

    return -1


print(first_unique_char("leetcode"))  # 0
print(first_unique_char("loveleetcode"))  # 2
print(first_unique_char("aabbcc"))  # -1
print(first_unique_char("aabccbd"))  # 6 ('d')
