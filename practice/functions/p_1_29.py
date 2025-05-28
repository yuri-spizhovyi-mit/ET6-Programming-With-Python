from itertools import permutations


def generate_all_strings():
    chars = ["c", "a", "t", "d", "o", "g"]
    all_perms = permutations(chars)  # Generates tuples of all permutations
    for p in all_perms:
        print("".join(p))  # Convert tuple to string


generate_all_strings()


def generate_permutations(chars, path="", used=None):
    if used is None:
        used = [False] * len(chars)

    if len(path) == len(chars):
        print(path)
        return

    for i in range(len(chars)):
        if not used[i]:
            used[i] = True
            generate_permutations(chars, path + chars[i], used)
            used[i] = False  # backtrack


# Run it
chars = ["c", "a", "t", "d", "o", "g"]
generate_permutations(chars)
