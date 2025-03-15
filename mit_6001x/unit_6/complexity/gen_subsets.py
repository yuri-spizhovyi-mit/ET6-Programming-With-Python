def gen_subsets(L):
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = gen_subsets(L[:-1])  # all subsets without last element
    extra = L[-1:]  # create a list of just last element
    new = []
    for small in smaller:
        new.append(
            small + extra
        )  # for all smaller solutions, add one with last element
    return smaller + new


print(gen_subsets([1, 2, 3, 4, 5, 6, 7, 8]))
