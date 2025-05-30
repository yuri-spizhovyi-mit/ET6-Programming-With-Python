def fib_seq(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    return a


fib_sequence = fib_seq(10)
print(fib_sequence)
