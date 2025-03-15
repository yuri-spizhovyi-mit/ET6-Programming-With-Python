def fib_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n - 1):
            temp = fib_i
            fib_i = fib_ii
            fib_ii = temp + fib_ii
        return fib_ii


print(fib_iterative(8))
