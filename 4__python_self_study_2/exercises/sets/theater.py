"""
Seat Allocation in a Theater
Generate all possible seat combination in a theater with rows
and columns"""

from itertools import product

rows = {"A", "B", "C"}
columns = {1, 2, 3}
all_seats = sorted(list(set(product(rows, columns))))
print("All Seats: ", all_seats)
