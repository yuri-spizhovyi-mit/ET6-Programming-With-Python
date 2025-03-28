def gen_powerset(items):
    n = len(items)
    result = []
    for i in range(2**n):
        combo = []
        for j in range(n):
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        result.append(combo)
    return result


n = ["a", "b", "c"]
print(gen_powerset(n))
