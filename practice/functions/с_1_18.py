def sequence_generator():
    num = 0
    result = []
    for i in range(0, 10):
        num += 2 * i
        result.append(num)
    return result


print(sequence_generator())


def sequence_generator2():
    return [sum(2 * j for j in range(i + 1)) for i in range(10)]


print(sequence_generator2())
