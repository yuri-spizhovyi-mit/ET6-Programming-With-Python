def gcd(a, b):
    if a <= b:
        for i in range(a, 0, -1):
            if (a % i == 0) & (b % i == 0):
                return i
    else:
        for i in range(b, 0, -1):
            if (a % i == 0) & (b % i == 0):
                return i


print(gcd(462, 1071))
