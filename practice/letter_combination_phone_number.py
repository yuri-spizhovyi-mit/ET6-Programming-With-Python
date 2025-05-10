def letterCombinations(digits):
    if not digits:
        return []

    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = [""]  # Start with an empty combination
    for digit in digits:
        letters = phone_map[digit]
        temp = []
        for prefix in result:
            for letter in letters:
                temp.append(prefix + letter)
        result = temp

    return result
