def max_contig_sum_reuse_sum(L):
    max_sum = L[0]
    n = len(L)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += L[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


L = [3, 4, -1, 5, -4]
print(max_contig_sum_reuse_sum(L))
