def modSwapSort(L):
    """L is a list on integers"""
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)


L = [4, 1, 4, 1, 4, 1]
modSwapSort(L)
