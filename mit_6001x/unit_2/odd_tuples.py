def odd_tuples(a_tuple):
    odd = ()
    for i, value in enumerate(a_tuple):
        if i % 2 == 0:
            odd = odd + (value,)
    return odd


print(odd_tuples(("I", "am", "a", "test", "tuple")))
