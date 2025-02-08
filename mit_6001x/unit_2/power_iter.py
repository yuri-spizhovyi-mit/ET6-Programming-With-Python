# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0

#     returns: int or float, base^exp
#     '''
#     # Your code here
#     result = 1
#     for i in range(1, exp + 1):
#         result *= base
#     return result

# print(iterPower(2, 3))


def recurPower(base, exp):
    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)


print(recurPower(2, 3))
