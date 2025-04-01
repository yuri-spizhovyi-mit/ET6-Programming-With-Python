# 1. Define the items (name, value, weight)
items = [("A", 60, 10), ("B", 100, 20), ("C", 120, 30)]

# 2. Calculate value-to-weight ratio for each item
items_with_density = []
for name, value, weight in items:
    ratio = value / weight
    items_with_density.append((name, value, weight, ratio))

# 3. Sort items by value-to-weight ratio in descending order
items_sorted = sorted(items_with_density, key=lambda x: x[2], reverse=True)

# 4. Greedy selection
max_weight = 50
total_value = 0
total_weight = 0
taken_items = []

for name, value, weight, ratio in items_sorted:
    if total_weight + weight <= max_weight:
        taken_items.append(name)
        total_value += value
        total_weight += weight

# 5. Show result
print("Items taken:", taken_items)
print("Total value:", total_value)
print("Total weight:", total_weight)
