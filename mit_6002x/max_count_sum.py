def max_contig_sum_with_subarray(L):
    current_sum = max_sum = L[0]
    start = end = start_temp = 0

    for i in range(1, len(L)):
        if L[i] > current_sum + L[i]:
            current_sum = L[i]
            start_temp = i  # start new subarray here
        else:
            current_sum += L[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = start_temp
            end = i  # update the actual best range

    return max_sum, L[start : end + 1]
