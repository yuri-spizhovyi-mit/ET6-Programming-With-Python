def h(n):
    """Assume n an int >=0"""
    answer = 0
    s = str(n)
    for c in s:
        answer += int(c)
    return answer


print(h(1234))
