def get_all_subsets_quick(some_list):
    subsets = [[]]
    for elem in some_list:
        subsets += [curr + [elem] for curr in subsets]

    return subsets


some_list = [1, 2]
print(get_all_subsets_quick(some_list))
