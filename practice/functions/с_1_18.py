def sequence_generator():
    num = 0
    result = []
    for i in range(0, 10):
        num += 2 * i
        result.append(num)
    return result


print(sequence_generator())
