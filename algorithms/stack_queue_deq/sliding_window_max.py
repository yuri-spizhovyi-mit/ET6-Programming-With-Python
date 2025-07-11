from collections import deque


def sliding_window_max(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove indices outside the window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller values from the end
        while dq and nums[i] > nums[dq[-1]]:
            dq.pop()

        dq.append(i)

        # Append max of window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Test
print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# ➜ [3, 3, 5, 5, 6, 7]
