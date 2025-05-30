from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits))) + 1
        return [int(d) for d in str(num)]


digits = [9, 9, 9]
s = Solution()
print(s.plus_one(digits))
