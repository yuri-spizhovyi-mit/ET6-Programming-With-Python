import numpy as np


def find_combination(choices, total):
    n = len(choices)
    best_fit = None

    exact_match_found = False
    fewest_items = float("inf")
    best_under_sum = -1

    for i in range(2**n):
        mask = bin(i)[2:].zfill(n)
        selection = np.array([int(b) for b in mask])
        selected_sum = np.dot(selection, choices)
        num_selected = np.sum(selection)

        if selected_sum == total:
            # exact match — only update if it's better (fewer items)
            if not exact_match_found or num_selected < fewest_items:
                best_fit = selection
                fewest_items = num_selected
                exact_match_found = True

        elif not exact_match_found and selected_sum < total:
            # no exact match yet — keep best under total
            if selected_sum > best_under_sum or (
                selected_sum == best_under_sum and num_selected < fewest_items
            ):
                best_fit = selection
                best_under_sum = selected_sum
                fewest_items = num_selected

    return best_fit


choices = [1, 2, 2, 3]
print(find_combination(choices, 4))
