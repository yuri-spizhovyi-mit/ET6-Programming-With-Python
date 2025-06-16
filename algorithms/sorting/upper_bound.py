def upper_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left - 1  # Step back to the last valid index
nums = [1, 3, 5, 7, 9, 11]
print(upper_bound(nums, 7))  # Output: 3
print(upper_bound(nums, 4))  # Output: -1