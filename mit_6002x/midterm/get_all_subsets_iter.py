def get_all_subsets_iterative(some_list):
    subsets = [[]]
    for elem in some_list:
        new_subsets = []
        for existing_subset in subsets:
            new_subset = existing_subset + [elem]
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)

    return subsets


some_list = [1, 2]
print(get_all_subsets_iterative(some_list))
