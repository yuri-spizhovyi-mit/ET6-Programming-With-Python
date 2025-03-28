def gen_powerset(items):
    n = len(items)
    knapsack_1 = []
    knapsack_2 = []
    for i in range(3**n):
        combo_1 = []
        combo_2 = []
        skipped = []
        for j in range(n):
            digit = (i // (3**j)) % 3
            if digit == 0:
                skipped.append(items[j])
            elif digit == 1:
                combo_1.append(items[j])
            elif digit == 2:
                combo_2.append(items[j])
        knapsack_1.append(combo_1)
        knapsack_2.append(combo_2)
    return knapsack_1, knapsack_2


n = ["a", "b"]
print(gen_powerset(n))
