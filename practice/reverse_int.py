class Solution:
    def reverse(self, x: int) -> int:
        multiplier = -1 if x < 0 else 1
        x = str(abs(x))
        x = int(x[::-1])
        x = multiplier * x
        return 0 if x > 2**31 - 1 or x < -(2**31) else x


s = Solution()
print(s.reverse(-123))
