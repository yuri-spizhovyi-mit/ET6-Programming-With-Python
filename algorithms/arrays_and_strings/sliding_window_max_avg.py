"""
A “sliding window” is a subarray that moves (or “slides”) across
a larger array or string to track something: sum, max, unique chars, etc.
Use it when:
You're scanning a contiguous segment of the array/string
And want to avoid recalculating from scratch every time

Classic Problem: Maximum Average Subarray I
Find the maximum average of a subarray of length k.

Input: nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75
Explanation: max average is from subarray [12, -5, -6, 50]
"""


def find_max_average(nums: list[int], k: int) -> float:
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k


print(find_max_average([1, 12, -5, -6, 50, 3], 4))
