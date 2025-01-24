# Builder notation
A = {-2, 0, 1, 4}
B = {x for x in A if x > 0}
print(B)

# Empty set


def elements(A):
    if A == set():
        print("A is the empty set")
    else:
        for x in A:
            print(x, "is an element of the set")


X = set()
elements(X)
B = {1, 2}
elements(B)

# The cardinality of a set A

A = {2, 2, 3, 3, 5, 5, 8, 8}
B = set()
C = {0}
D = {2, 3, 5, 8}
print("The cardinality of A: ", len(A))
print("The cardinality of B: ", len(B))
print("The cardinality of C: ", len(C))
if A == D:
    print("A equals D")

# Subset in Python

A = {1, 2, 3}
B = {1, 2}
print("A is a subset of B: ", A.issubset(B))
print("B is a subset of A: ", B.issubset(A))
print("B <= A: ", B <= A)

# Union

A = {-3, -1, 2, 5}
B = {-1, 0, 2}
print("Union: ", A.union(B))
print("Union: ", A | B)

# Intersection

print("Intersection A and B: ", A.intersection(B))
print("Intersection A & B: ", A & B)

A = {"a"}
C = {"c"}
print(A & C)
