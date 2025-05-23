def sum_positive_squares(n: int) -> int:
    if n <= 0:
        raise ValueError("Input must be positive")
    num_less_n = n - 1
    result = 0
    while num_less_n > 0:
        result += num_less_n**2
        num_less_n -= 1

    return result


if __name__ == "__main__":
    print(sum_positive_squares(3))
