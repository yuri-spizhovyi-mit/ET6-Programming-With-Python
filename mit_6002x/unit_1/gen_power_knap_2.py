def yieldAllCombos(items):
    n = len(items)
    for i in range(3**n):
        combo_1 = []
        combo_2 = []
        for j in range(n):
            digit = (i // (3**j)) % 3
            if digit == 1:
                combo_1.append(items[j])
            elif digit == 2:
                combo_2.append(items[j])
        yield combo_1, combo_2


n = ["a", "b"]
gp = yieldAllCombos(n)
print(gp.__next__())
print(gp.__next__())
print(gp.__next__())
print(gp.__next__())
