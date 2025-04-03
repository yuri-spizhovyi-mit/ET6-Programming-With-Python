def max_value(items, avail):
    # Base case: no more items or no more capacity
    if not items or avail == 0:
        return 0, []

    name, value, weight = items[0]

    if weight > avail:
        # Skip item if too heavy
        return max_value(items[1:], avail)
    else:
        # Option 1: Take the item
        with_val, with_items = max_value(items[1:], avail - weight)
        with_val += value

        # Option 2: Skip the item
        without_val, without_items = max_value(items[1:], avail)

        # Choose the better option
        if with_val > without_val:
            return with_val, with_items + [name]
        else:
            return without_val, without_items


# Test
items = [("A", 60, 10), ("B", 100, 20), ("C", 120, 30)]

max_weight = 50
val, taken = max_value(items, max_weight)

print("Items taken:", taken)
print("Total value:", val)


items = [("A", 60, 10), ("B", 100, 20), ("C", 120, 30)]

max_weight = 50
val, taken = max_value(items, max_weight)

print("\nRESULT:")
print("Items taken:", taken)
print("Total value:", val)
