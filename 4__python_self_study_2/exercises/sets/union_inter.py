set_1 = {1, 2, 3}
set_2 = {3, 4, 5}

# Union
print(set_1.union(set_2))  # {1, 2, 3, 4, 5}
set_3 = set_1 | set_2
print("Set 3: ", set_3)  # {3, 4, 5}

# Intersection
print(set_1.intersection(set_2))  # {3}
set_4 = set_1 & set_2
print("Set 4: ", set_4)

# Difference
print(set_1.difference(set_2))  # {1, 2}

# Symmetric Difference
print(set_1.symmetric_difference(set_2))  # {1, 2, 4, 5}
