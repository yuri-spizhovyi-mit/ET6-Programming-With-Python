def max_sum(L):
    current_sum = max_sum = L[0]
    for num in L[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


L = [3, 4, -1, 5, -4]
print(max_sum(L))
