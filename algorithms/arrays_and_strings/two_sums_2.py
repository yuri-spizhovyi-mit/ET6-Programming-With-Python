def two_sum(nums: list[int], target: int) -> list[int]:
    index_map = {}  # number → index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i
