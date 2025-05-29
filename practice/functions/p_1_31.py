def make_change(given, charged):
    """Program take two numbers as input, one that is a monetary amount charged and the
    other that is a monetary amount given. Bills and monetary: Canada.
    Inputs: given, charged
    Outputs: the change
    """
    bills = [100.00, 50.00, 20.00, 10.00, 5.00]
    coins = [2.00, 1.00, 0.25, 0.10, 0.05, 0.01]
    result = {}
    change = round(given - charged, 2)
    if change < 0:
        raise ValueError("Given amount is less than charged amount.")

    for bill in bills:
        while change >= bill:
            result[bill] = result.get(bill, 0) + 1
            change -= bill
            change = round(change, 2)

    for coin in coins:
        while change >= coin:
            result[coin] = result.get(coin, 0) + 1
            change -= coin

    return result


# print(make_change(201.10, 100))


def make_change_pro(given, charged):
    """Return optimal change as few coins and bills as possible (CAD)."""
    # Convert to cents to avoid floating point issues
    change_cents = round((given - charged) * 100)

    if change_cents < 0:
        raise ValueError("Given amount is less than the charged amount.")

    # Denominations in cents
    denominations = {
        10000: "$100",
        5000: "$50",
        2000: "$20",
        1000: "$10",
        500: "$5",
        200: "Toonie ($2)",
        100: "Loonie ($1)",
        25: "Quarter (0.25)",
        10: "Dime (0.10)",
        5: "Nickel (0.05)",
        1: "Penny (0.01)",
    }

    result = {}
    for value, name in denominations.items():
        count = change_cents // value
        if count > 0:
            result[name] = count
            change_cents -= count * value

    return result


# Example:
print(make_change_pro(201.10, 100))
