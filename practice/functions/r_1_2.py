def is_even(k):
    k = abs(k)
    while k > 1:
        k -= 2
        return k == 0


if __name__ == "__main__":
    print(is_even(3))  # False
    print(is_even(4))  # True
    print(is_even(-2))  # True
