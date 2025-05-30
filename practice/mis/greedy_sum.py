def greedySum(L, s):
    total_mult = 0
    remain = s

    for num in L:
        mult = remain // num
        total_mult += mult
        remain -= num * mult

    return total_mult if remain == 0 else "no solution"
