from collections import OrderedDict


class StringAnalyzer:
    def __init__(self, text: str):
        self.text = text

    def first_unique_char(self) -> str:
        seen = OrderedDict()

        for i, char in enumerate(self.text):
            if char in seen:
                seen[char] = (seen[char][0] + 1, seen[char][1])
            else:
                seen[char] = (1, i)

        for char, (count, index) in seen.items():
            if count == 1:
                return char

        return "_"

    @property
    def length(self) -> int:
        return len(self.text)

    def __str__(self):
        return f"Analyzing string: '{self.text}'"


s1 = StringAnalyzer("leetcode")
print(s1)  # ➞ Analyzing string: 'leetcode'
print(s1.first_unique_char())  # ➞ "l"
print(s1.length)  # ➞ 8

s2 = StringAnalyzer("aabbcc")
print(s2.first_unique_char())  # ➞ "_"
