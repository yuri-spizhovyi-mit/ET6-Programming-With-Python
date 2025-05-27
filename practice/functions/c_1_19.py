import string


def alphabet_generator():
    return [x for x in string.ascii_lowercase]


print(alphabet_generator())


def alphabet_generator2():
    return [chr(i) for i in range(ord("A"), ord("z") + 1)]


print(alphabet_generator2())
