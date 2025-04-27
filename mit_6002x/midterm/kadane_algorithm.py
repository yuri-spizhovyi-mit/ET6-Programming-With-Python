def max_contig_sum(L):
    current_sum = max_sum = L[0]
    for num in L[1:]:
        current_sum = max(num, num + current_sum)
        max_sum = max(max_sum, current_sum)

    return max_sum


L = [3, 4, -8, 15, -1, 2]
print(max_contig_sum(L))
