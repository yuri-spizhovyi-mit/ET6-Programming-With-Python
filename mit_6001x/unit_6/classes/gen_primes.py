def genPrimesFn():
    """Function to return 1000000 prime numbers"""
    primes = []  # primes generated so far
    last = 1  # last number tried
    while len(primes) < 100:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
    return primes


print(genPrimesFn())
