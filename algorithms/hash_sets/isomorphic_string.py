def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for sc, tc in zip(s, t):
        if (sc in s_to_t and s_to_t[sc] != tc) or (tc in t_to_s and t_to_s[tc] != sc):
            return False

        s_to_t[sc] = tc
        t_to_s[tc] = sc
    return True


print(is_isomorphic("egg", "add"))  # True
print(is_isomorphic("foo", "bar"))  # False
print(is_isomorphic("paper", "title"))  # True
print(is_isomorphic("ab", "aa"))  # False (a→a, b→a ❌)
