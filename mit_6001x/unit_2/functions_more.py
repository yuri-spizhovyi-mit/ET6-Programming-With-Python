import math


def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.14]

apply_to_each(L, abs)
print(L)
apply_to_each(L, int)
print(L)
