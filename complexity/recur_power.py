def recurPowerNew(a, b):
    print(a, b)
    if b == 0:
        return 1
    elif b % 2 == 0:
        return recurPowerNew(a * a, b / 2)
    else:
        return a * recurPowerNew(a, b - 1)


print(recurPowerNew(2, 3))
