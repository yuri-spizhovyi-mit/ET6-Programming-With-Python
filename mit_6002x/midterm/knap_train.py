def knap_greedy(
    weight: list[int], values: list[int], max_weight: int
) -> list[tuple[int, int]]:
    # Step 1: Pack each weight and value together:
    items = list(zip(weight, values))

    # Step 2: Sort list of items in descending order by value/weight ratio
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    # Step 3: Initialize total weight and total value variables
    total_weight, total_value = 0, 0

    # Step 4: Prepare a list of selected items
    selected_items = []

    # Step 5: Greedly select items
    for weight, value in items:
        # Choose an item if it does not exceed total weight
        if weight + total_weight <= max_weight:
            selected_items.append((weight, value))
            total_value += value
            total_weight += weight

    return selected_items


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
max_weight = 5

print(knap_greedy(weights, values, max_weight))
