class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a, 2)
        b_int = int(b, 2)
        total = a_int + b_int
        return bin(total)[2:]


s = Solution()
print(s.addBinary("11", "10"))
