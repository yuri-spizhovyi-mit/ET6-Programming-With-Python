from collections import Counter


def sort_unique_by_frequency(nums):
    freq = Counter(nums)
    # Use set(nums) or freq.keys() to get unique elements
    unique = list(freq.keys())
    return sorted(unique, key=lambda x: (-freq[x], x))


nums = [4, 5, 6, 5, 4, 3]
print(sort_unique_by_frequency(nums))
# ➜ [4, 5, 3, 6]
