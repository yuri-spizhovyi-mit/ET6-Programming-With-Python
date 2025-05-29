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


print(make_change(201.10, 100))
