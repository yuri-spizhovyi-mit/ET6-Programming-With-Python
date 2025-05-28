def check_index_error_on_write():
    l1 = [1, 2, 3]
    try:
        l1[3] = 99
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")


check_index_error_on_write()
