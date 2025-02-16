# L1 = [1, 28, 36]
# L2 = [2, 57, 9]

# for elt in map(min, L1, L2):
#   print(elt)


def square(a):
    return a * a


def halve(a):
    return a / 2


def inc(a):
    return a + 1


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


print(applyEachTo([inc, square, halve, abs], -3))
