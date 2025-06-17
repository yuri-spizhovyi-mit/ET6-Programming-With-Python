def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found


nums = [1, 3, 5, 7, 9, 11]
print(binary_search(nums, 7))  # Output: 3
print(binary_search(nums, 4))  # Output: -1
