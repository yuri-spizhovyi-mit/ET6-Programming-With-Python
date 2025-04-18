def bisection_search(L: list, e: int) -> bool:
    if not L:
        return False

    mid = len(L) // 2
    if L[mid] == e:
        return True
    elif L[mid] > e:
        return bisection_search(L[:mid], e)
    else:
        return bisection_search(L[mid + 1 :], e)


L = [1, 2, 3, 5, 8]
e = 8
print(bisection_search(L, e))
