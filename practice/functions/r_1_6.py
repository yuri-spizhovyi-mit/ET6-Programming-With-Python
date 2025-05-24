def sum_squared_positive_odd(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return sum([x**2 for x in range(1, n) if x % 2 == 1])


if __name__ == "__main__":
    print(sum_squared_positive_odd(6))
