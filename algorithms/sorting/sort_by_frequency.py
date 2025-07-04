from collections import Counter


def sort_by_frequency(nums: list[int]) -> list[int]:
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (-freq[x], x))


print(sort_by_frequency([4, 5, 6, 5, 4, 3]))
# ➜ [4, 4, 5, 5, 3, 6]

print(sort_by_frequency([2, 3, 1, 3, 2]))
# ➜ [2, 2, 3, 3, 1]
