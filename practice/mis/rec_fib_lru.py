from functools import lru_cache


@lru_cache(maxsize=None)
def rec_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rec_fib(n - 1) + rec_fib(n - 2)


print(rec_fib(7))
