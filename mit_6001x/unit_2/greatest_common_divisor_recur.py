# def gcd(a, b):
#     if a > b:
#         a, b = b, a
#     if a == 1:
#         return a
#     else:
#         if b % a == 0:
#             return a
#         else:
#             return gcd(a - 1, b)


# print(gcd(77,42))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(1071, 462))
