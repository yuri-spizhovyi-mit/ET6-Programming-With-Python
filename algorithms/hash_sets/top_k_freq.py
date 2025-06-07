from collections import Counter
import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

print(top_k_frequent([1,1,1,2,2,3], 2))  # [1, 2]
print(top_k_frequent([1], 1))           # [1]
print(top_k_frequent([4,4,4,6,6,7,7,7], 2))  # [4, 7] or [7, 4]
