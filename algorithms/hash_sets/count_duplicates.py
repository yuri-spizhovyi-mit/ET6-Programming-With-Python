def count_duplicates(nums: list[int]) -> int:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    duplicates = 0
    for count in freq.values():
        if count > 1:
            duplicates += 1

    return duplicates


print(count_duplicates([1, 2, 2, 3, 4, 4, 4, 5]))  # 2
print(count_duplicates([1, 1, 1, 1]))  # 1
print(count_duplicates([1, 2, 3, 4]))  # 0
