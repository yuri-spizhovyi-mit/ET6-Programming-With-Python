def sum_positive_squares(n: int) -> int:
    if n <= 0:
        raise ValueError("Input must be positive")

    return sum([i**2 for i in range(1, n)])


if __name__ == "__main__":
    print(sum_positive_squares(3))
