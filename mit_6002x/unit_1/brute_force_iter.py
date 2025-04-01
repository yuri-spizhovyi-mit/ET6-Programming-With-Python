from itertools import combinations

# Define items: (name, value, weight)
items = [
    ("A", 60, 10),
    ("B", 100, 20),
    ("C", 120, 30)
]

max_weight = 50
best_value = 0
best_combo = []

# Try all possible combinations of items (from 0 to all items)
for r in range(len(items) + 1):
    for combo in combinations(items, r):
        total_weight = sum(item[2] for item in combo)
        total_value = sum(item[1] for item in combo)

        if total_weight <= max_weight and total_value > best_value:
            best_value = total_value
            best_combo = combo

# Show result
print("Items taken:", [item[0] for item in best_combo])
print("Total value:", best_value)
print("Total weight:", sum(item[2] for item in best_combo))
