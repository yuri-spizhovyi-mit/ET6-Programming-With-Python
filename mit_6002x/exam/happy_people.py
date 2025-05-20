income = [10, 30, 90, 100, 120, 60]
distance_from_np = [4, 10, 5, 1, 1, 6]
persons = ["p1", "p2", "p3", "p4", "p5", "p6"]

result = {}


def calculate_distance(income, distance_from_np, persons):
    if len(income) == 1:
        return 0
    for i in range(1, len(income)):
        dist = abs(distance_from_np[0] - distance_from_np[i]) + abs(
            income[0] - income[i]
        )
        p_to_p = persons[0] + persons[i]
        result[p_to_p] = dist
    calculate_distance(income[1:], distance_from_np[1:], persons[1:])
    minim = min(result.items(), key=lambda x: x[1])

    maxim = max(result.items(), key=lambda x: x[1])
    return minim, maxim


print(calculate_distance(income, distance_from_np, persons))
