import itertools


def get_all_subsets_itertools(some_list):
    subsets = []
    for r in range(len(some_list) + 1):
        for combo in itertools.combinations(some_list, r):
            subsets.append(list(combo))
    return subsets


some_list = [1, 2]
print(get_all_subsets_itertools(some_list))
