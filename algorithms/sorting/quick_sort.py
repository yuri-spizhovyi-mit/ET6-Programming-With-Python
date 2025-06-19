def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  #
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([9, 3, 7, 1, 6]))
# ➜ [1, 3, 6, 7, 9]