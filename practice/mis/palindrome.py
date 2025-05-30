class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


s = Solution()

print(s.isPalindrome(22))
