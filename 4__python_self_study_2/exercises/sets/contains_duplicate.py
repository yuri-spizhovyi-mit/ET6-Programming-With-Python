from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


result = Solution().containsDuplicate([1, 2, 3, 1])
print(result)  # True
