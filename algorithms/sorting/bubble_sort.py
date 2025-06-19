def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # track if any swap occurred
        for j in range(n - 1 - i):  # skip sorted tail
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                swapped = True
        if not swapped:  # if not swaps, list is sorted
            break
    return arr


# Test
print(bubble_sort([5, 1, 4, 2, 3]))  # ➜ [1, 2, 4, 5, 8]
