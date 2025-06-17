def min_subarray_len(target, nums):
    left, right = 1, len(nums) + 1  # +1 to allow inclusive search
    answer = 0

    def meets_condition(length):
        window_sum = sum(nums[:length])
        if window_sum >= target:
            return True
        for i in range(length, len(nums)):
            window_sum += nums[i] - nums[i - length]
            if window_sum >= target:
                return True
        return False

    while left < right:
        mid = (left + right) // 2
        if meets_condition(mid):
            right = mid
        else:
            left = mid + 1

    return left if left <= len(nums) else 0


nums = [1, 3, 5, 7, 9, 11]
print(min_subarray_len(7, nums))  # Output: 3
print(min_subarray_len(4, nums))  # Output: 2
