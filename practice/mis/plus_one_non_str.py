from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in reversed(range(n)):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + [0] * n


digits = [9, 9, 9]
s = Solution()
print(s.plus_one(digits))
