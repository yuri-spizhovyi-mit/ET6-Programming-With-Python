def minCostClimbingStairs(cost):
    a, b = 0, 0
    for i in range(2, len(cost) + 1):
        a, b = b, min(b + cost[i - 1], a + cost[i - 2])
    return b


cost = [10, 15, 20]
print(minCostClimbingStairs(cost))
