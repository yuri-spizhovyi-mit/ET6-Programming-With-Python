def last_occurrence(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid
            left = mid + 1  # Keep looking right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
nums = [1, 3, 5, 7, 9, 11]
print(last_occurrence(nums, 7))  # Output: 3
print(last_occurrence(nums, 4))  # Output: -1