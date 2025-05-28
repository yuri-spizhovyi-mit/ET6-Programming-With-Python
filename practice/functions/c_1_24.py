def count_vowels(s):
    vowels = {"a", "e", "i", "o", "u", "y"}
    return sum([1 for char in s.lower() if char in vowels])


print(count_vowels("Yello"))
