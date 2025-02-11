te = ()


def q_and_r(x, y):
    q = x // y
    r = x % y
    return (q, r)


(quot, rem) = q_and_r(4, 5)
print(quot, rem)
x = (1, 2, (3, "John", 4), "Hi")
print(type(x[2][2]))
