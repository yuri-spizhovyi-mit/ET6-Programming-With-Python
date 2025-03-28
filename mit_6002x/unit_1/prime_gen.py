def gen_prime():
    primes = []
    num = 2
    while True:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if (num % p) == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            yield num
        num += 1


gp = gen_prime()
print(gp.__next__())
print(gp.__next__())
print(gp.__next__())
print(gp.__next__())
print(gp.__next__())
