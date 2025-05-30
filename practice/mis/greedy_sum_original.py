def greedySum(L, s):
    """
    input:
        s: positive integer, the target sum
        L: list of unique positive integers sorted in descending order
    Uses a greedy approach to solve:
        s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
    return: sum of multipliers if possible, else 'no solution'
    """
    multipliers = []
    remain = s

    for i in L:
        mult = remain // i
        multipliers.append(mult)
        remain -= i * mult

    if remain == 0:
        return sum(multipliers)
    else:
        return "no solution"


# print(greedySum([10, 5, 1], 14))  # 14 = 10*1 + 5*0 + 1*4 Output: 5
# print(greedySum([10, 5, 1], 23))  # 23 = 10*2 + 5*0 + 1*3 Output: 5
# print(greedySum([9, 6], 8))  # No solution

L = [6, 4, 3]
s = 8
print(greedySum(L, s))
