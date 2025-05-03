"""Efficient Algorithm (Kadane’s Algorithm)"""


def max_contig_sum(L):
    """L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L"""
    current_sum = max_sum = L[0]
    for num in L[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


L = [3, 4, -1, 5, -4]
print(max_contig_sum(L))
