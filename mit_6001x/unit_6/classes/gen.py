def generator1():
    if True:
        yield 1


def generator2():
    if False:
        yield 1


g1 = generator1()
g2 = generator2()

print(type(g1))
print(type(g2))
print(g1.__next__())
print(g1.__next__())
# print(g2.__next__())
