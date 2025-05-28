def dot_product(l1: list, l2: list):
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i] * l2[i])
    return l3


print(dot_product([1, 3, 3], [3, 2, 1]))


def dot_product_map(l1: list, l2: list):
    return list(map(lambda a, b: a * b, l1, l2))


print(dot_product_map([4, 5, 6], [6, 5, 4]))


def dot_product_zip(l1, l2):
    return [a * b for a, b in zip(l1, l2)]


print(dot_product_zip([1, 1, 1], [2, 2, 2]))
