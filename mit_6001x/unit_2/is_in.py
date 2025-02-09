def is_in(char, a_str):
    middle = len(a_str) // 2
    if len(a_str) <= 1 and (char == a_str):
        return True
    if len(a_str) <= 1 and (char != a_str):
        return False
    elif char == a_str[middle]:
        return True
    elif char > a_str[middle]:
        return is_in(char, a_str[middle:])
    else:
        return is_in(char, a_str[:middle])


print(is_in("a", ""))
