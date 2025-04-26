def greedy_knapsack(weight, values, max_weight):
    # Step 1: Pack weight and its corresponding value together
    # This creates pairs like (weight, value)
    items = list(zip(weight, values))

    # Step 2: Sort items by "value-to-weight ratio" descending order
    # Higher value/weight comes first (greedy choice)
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    # Step 3: Initialize total value and total weight
    total_value, total_weight = 0, 0

    # Step 4: Prepare a list to store selected (weight, value) pairs
    selected_items = []

    # Step 5: Greedy select items
    for weight, value in items:
        # If adding the item does not exceed max_weight
        if total_weight + weight <= max_weight:
            selected_items.append((weight, value))
            total_weight += weight
            total_value += value

    # Step 6: Return the selected items and the total value

    return selected_items, total_value


weights = [10, 2, 3, 4, 5, 1]
values = [10, 3, 4, 5, 6, 1]
max_weight = 5

selected_items, total_value = greedy_knapsack(values, weights, max_weight)
print(f"Selected items (weight, value):{selected_items}")
print(f"Total value: {total_value}")
