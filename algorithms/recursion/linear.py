def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S"""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]


S = [1, 2, 3, 4, 5]
print(linear_sum(S, 3))
