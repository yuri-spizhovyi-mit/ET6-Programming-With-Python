class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i : i + n] == needle:
                return i

        return -1


haystack = "tsad"
needle = "sad"
s = Solution()
print(s.strStr(haystack, needle))
