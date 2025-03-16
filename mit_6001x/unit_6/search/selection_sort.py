def ss(L):
    for i in range(len(L) - 1):
        print(L)
        # Extract min element
        min_el_ind = i
        min_el = L[i]
        j = i + 1
        # Swap it with current element
        while j < len(L):
            if min_el > L[j]:
                min_el_ind = j
                min_el = L[j]
            j += 1
        temp = L[i]
        L[i] = L[min_el_ind]
        L[min_el_ind] = temp


L = [3, 2, 1, 1, 2, 3]
print(ss(L))
