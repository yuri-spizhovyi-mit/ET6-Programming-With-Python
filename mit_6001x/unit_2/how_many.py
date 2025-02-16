# animals = {'B': [15], 'u': [10, 15, 5, 2, 6]}
animals = {"a": ["aardvark", 0], "b": ["baboon", 1], "c": ["coati", "coati"]}


def how_many(animals):
    count = 0
    lv = animals.values()
    for i in lv:
        for j in i:
            count += 1
    return count


print(how_many(animals))
