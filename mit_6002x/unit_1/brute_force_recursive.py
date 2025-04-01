def max_value(items, avail, depth=0):
    indent = "  " * depth  # indentation to visualize recursion level

    # Print current call
    print(
        f"{indent}max_value(items={[(i[0], i[1], i[2]) for i in items]}, avail={avail})"
    )

    # Base case: no more items or no more capacity
    if not items or avail == 0:
        print(f"{indent}Returning (0, [])")
        return 0, []

    name, value, weight = items[0]

    if weight > avail:
        print(f"{indent}Skipping {name}, too heavy")
        return max_value(items[1:], avail, depth + 1)
    else:
        # Option 1: take the item
        print(f"{indent}Considering {name}, trying to take it")
        with_val, with_items = max_value(items[1:], avail - weight, depth + 1)
        with_val += value

        # Option 2: skip the item
        print(f"{indent}Considering {name}, trying to skip it")
        without_val, without_items = max_value(items[1:], avail, depth + 1)

        # Choose the better option
        if with_val > without_val:
            print(f"{indent}Taking {name} leads to better value: {with_val}")
            return with_val, with_items + [name]
        else:
            print(
                f"{indent}Skipping {name} leads to better or equal value: {without_val}"
            )
            return without_val, without_items


items = [("A", 60, 10), ("B", 100, 20), ("C", 120, 30)]

max_weight = 50
val, taken = max_value(items, max_weight)

print("\nRESULT:")
print("Items taken:", taken)
print("Total value:", val)
