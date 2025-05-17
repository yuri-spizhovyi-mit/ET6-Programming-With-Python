from typing import List

price = [13, 5, 1, 8, 21, 2]
k = 3


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        if k <= 1:
            return max(price)
        elif k == 2:
            return max(price) - min(price)
        else:
            next_index = int(len(price) / (k - 1))
            return min(
                abs(price[0] - price[next_index]), abs(price[-1] - price[-next_index])
            )


s = Solution()
print(s.maximumTastiness(price, k))
