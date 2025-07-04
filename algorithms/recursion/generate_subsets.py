def generate_subsets(s):
    if len(s) == 0:
        return [[]]
    else:
        first = s[0]
        rest_subsets = generate_subsets(s[1:])
        return rest_subsets + [[first] + subset for subset in rest_subsets]


s = [1, 2, 3]
print(generate_subsets(s))
