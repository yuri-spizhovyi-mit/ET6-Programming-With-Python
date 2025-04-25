def fib_iter(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, cur = 0, 1
    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur
        print(cur)
    return cur


print(fib_iter(7))
