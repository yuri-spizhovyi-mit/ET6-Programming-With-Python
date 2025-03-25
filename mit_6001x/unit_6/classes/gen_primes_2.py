def genPrimes():
    primes = []
    candidate = 2
    while True:
        check_primes = []
        for p in primes:
            if candidate % p != 0:
                check_primes.append(True)
            else:
                check_primes.append(False)
        if False not in check_primes:
            primes.append(candidate)
            yield candidate

        candidate += 1


gp = genPrimes()
print(gp.__next__())
print(gp.__next__())

# def genPrimes():
#     primes = []
#     candidate = 2
#     while True:
#         is_prime = all(candidate % p != 0 for p in primes)

#         if is_prime:
#             primes.append(candidate)
#             yield candidate

#         candidate += 1
