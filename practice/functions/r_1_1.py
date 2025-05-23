def is_multiple(n: int, m: int) -> bool:
    if m == 0:
        raise ValueError("The second argument must not be zero.")
    return n % m == 0


if __name__ == "__main__":
    print(is_multiple(4, 2))
