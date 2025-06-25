def string_revers(s):
    if len(s) <= 1:
        return s
    return string_revers(s[1:]) + s[0]

print(string_revers('pots'))