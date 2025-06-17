def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_inx = i  # assume first element is minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_inx]:
                min_inx = j  # update min index if found smaller
        arr[i], arr[min_inx] = arr[min_inx], arr[i]  # swap

    return arr


# Example
print(selection_sort([29, 10, 14, 37, 13]))  # Output: [10, 13, 14, 29, 37]
