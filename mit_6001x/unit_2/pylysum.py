import math


def polysum(n, s):
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    square_perimeter = (n * s) ** 2
    return round(area + square_perimeter, 4)

print(polysum(12, 2))
