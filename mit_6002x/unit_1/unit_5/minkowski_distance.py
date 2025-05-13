from scipy.spatial import distance

# Define two points
A = [2, 4, 5]
B = [1, 1, 1]

# Minkowski distance with p=3
p = 3
minkowski_dist = distance.minkowski(A, B, p)

print(f"Minkowski distance (p={p}):", minkowski_dist)
