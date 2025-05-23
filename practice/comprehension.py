result = {k: k * k for k in range(1, 5)}
print(result)
result_gen = (k * k for k in range(1, 5))
print(result_gen)
result_set = {k * k for k in range(1, 5)}
print(result_set)
print([k * k for k in range(1, 10, 2)])
