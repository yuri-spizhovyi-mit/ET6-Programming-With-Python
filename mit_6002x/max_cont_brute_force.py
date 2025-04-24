def max_contig_sum_brute_force(L):
    max_sum = L[0]  # start with the first element
    n = len(L)
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(L[i : j + 1])
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum
