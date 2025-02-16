a_list = [14, 12]
b_list = [2, "a", 4, True]
L = [2, 1, 3]
print(L)
M = L + b_list
print(M)
print(b_list.extend([1, 3, 4]))

a_list.extend(b_list)
print(a_list)
a_list = [14, 12]
print("a list", a_list)
