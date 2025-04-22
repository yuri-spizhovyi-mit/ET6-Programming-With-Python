from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index


nums = [3, 2, 2, 3]
val = 3

s = Solution()
print(s.removeElement(nums, val))
