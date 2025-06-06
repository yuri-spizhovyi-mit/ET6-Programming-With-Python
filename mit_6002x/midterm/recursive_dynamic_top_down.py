# Top-Down DP (Memoization)


def recursive_dynamic(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = recursive_dynamic(n - 1, memo) + recursive_dynamic(n - 2, memo)
    return memo[n]


for i in range(100):
    print(recursive_dynamic(i), end=" ")
