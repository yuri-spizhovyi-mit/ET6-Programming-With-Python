from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pass


digits = [1, 2, 3]
dg = ""
for num in digits:
    dg += str(num)
dg = int(dg) + 1
dg = str(dg)
result = []
for i in dg:
    result.append(i)

s = Solution()
print(result)

"""
1. Fetch last digit
2. Increase by 1
3. Replace last digit
4. In case the number will be 10 replase with [1, 0]

"""
