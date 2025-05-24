def list_range():
    result = [1]
    num = 1
    for i in range(1, 9):
        num += num
        result.append(num)
    return result


# print(list_range())


def lr_lc():
    return [2**x for x in range(9)]


print(lr_lc())
