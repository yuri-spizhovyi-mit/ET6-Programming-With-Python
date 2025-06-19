def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # change to > for descending
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append leftovers
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Test
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# ➜ [3, 9, 10, 27, 38, 43, 82]
