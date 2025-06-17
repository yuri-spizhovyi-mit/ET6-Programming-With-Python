def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # element to be inserted
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift right
            j -= 1
        arr[j + 1] = key  # insert
    return arr


# Test
print(insertion_sort([8, 4, 1, 5]))  # ➜ [1, 4, 5, 8]
