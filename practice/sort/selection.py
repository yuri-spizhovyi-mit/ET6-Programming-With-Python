def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current index holds the smallest value
        min_idx = i
        for j in range(i + 1, n):
            # Find the actual smallest value in the rest of the array
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the current element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Example
print(selection_sort([64, 25, 12, 22, 11]))  # Output: [11, 12, 22, 25, 64]
