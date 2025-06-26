from collections import Counter


def sort_element_freq_pairs(nums):
    freq = Counter(nums)
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))


nums = [4, 5, 6, 5, 4, 3]
print(sort_element_freq_pairs(nums))
# ➜ [(4, 2), (5, 2), (3, 1), (6, 1)]
