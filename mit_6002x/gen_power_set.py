def gen_powerset(items):
    n = len(items)
    result = []
    for i in range(n**2):
        combo = []
        for j in range(n):
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        result.append(combo)
    return result


n = ["a", "b"]
print(gen_powerset(n))
