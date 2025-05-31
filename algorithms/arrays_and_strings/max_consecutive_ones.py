def longest_ones(nums: list[int], k: int) -> int:
    left = 0
    max_length = 0
    zeros = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        # If we have more than k zeros, move left pointer
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


nums_list = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]

longest_ones(nums_list, 2)
