def min_max(data: list) -> tuple:
    if not data:
        raise ValueError("minmax() arg is empty sequence")

    min_val = data[0]
    max_val = data[0]

    for num in data[1:]:
        if num < min_val:
            min_val = num

        if num > max_val:
            max_val = num

    return (min_val, max_val)


if __name__ == "__main__":
    print(min_max([3, 20, 11, -5]))
