e = 5
L = [1, 2, 3, 4, 5]


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        elif L[i] > e:
            return False
    return False


search(L, e)
