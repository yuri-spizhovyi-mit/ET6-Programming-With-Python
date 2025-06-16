def lower_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left  # Or -1 if you want to check out-of-bound manually
nums = [1, 3, 5, 7, 9, 11]
print(lower_bound(nums, 7))  # Output: 3
print(lower_bound(nums, 4))  # Output: 2