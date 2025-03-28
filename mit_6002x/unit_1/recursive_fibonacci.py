def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fib(n - 1) + fib(n - 2)
    return result


for i in range(10):
    print(fib(i), end=" ")
