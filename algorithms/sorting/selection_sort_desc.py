def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_ind = i  # assume first element is minimum
        for j in range(i + 1, n):
            if arr[j] > arr[max_ind]:
                max_ind = j  # update min index if found smaller
        arr[i], arr[max_ind] = arr[max_ind], arr[i]  # swap

    return arr


# Example
print(selection_sort([29, 10, 14, 37, 13]))  # Output: [9, 6, 5, 5, 2, 1]

