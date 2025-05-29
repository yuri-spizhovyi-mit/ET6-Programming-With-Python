def two_divider_verbose(n):
    if n <= 2:
        raise ValueError("Number must be > 2")

    counter = 0
    print(f"Starting with: {n}")

    while n >= 2:
        n = n / 2
        counter += 1
        print(f"Step {counter}: {n}")

    print(f"\nTotal divisions before dropping below 2: {counter}")
    return counter


# Example
two_divider_verbose(10)
