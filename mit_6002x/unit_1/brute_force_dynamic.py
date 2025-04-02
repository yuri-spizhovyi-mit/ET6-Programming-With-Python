def max_value_memo(items, avail, index=0, memo=None):
    if memo is None:
        memo = {}

    # Memoization key: current index + remaining weight
    key = (index, avail)

    if key in memo:
        return memo[key]

    # Base case: no items left or no capacity
    if index >= len(items) or avail == 0:
        result = (0, [])
    elif items[index][2] > avail:
        # Skip item if too heavy
        result = max_value_memo(items, avail, index + 1, memo)
    else:
        name, value, weight = items[index]

        # Try taking the item
        with_val, with_items = max_value_memo(items, avail - weight, index + 1, memo)
        with_val += value

        # Try skipping the item
        without_val, without_items = max_value_memo(items, avail, index + 1, memo)

        # Choose better option
        if with_val > without_val:
            result = (with_val, with_items + [name])
        else:
            result = (without_val, without_items)

    memo[key] = result
    return result


items = [("A", 60, 10), ("B", 100, 20), ("C", 120, 30)]

max_weight = 50
val, taken = max_value_memo(items, max_weight)

print("Items taken:", taken)
print("Total value:", val)
