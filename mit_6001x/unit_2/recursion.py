# def mult_inter(a, b):
#   result = 0
#   while b > 0:
#     result += a
#     b -= 1
#   return result

# print(mult_inter(2, 2))

# def mult(a, b):
#   if b == 1:
#     return a
#   else:
#     return a + mult(a, b - 1)

# print(mult(2, 3))


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(3))


def fact_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


print(fact_iter(3))
