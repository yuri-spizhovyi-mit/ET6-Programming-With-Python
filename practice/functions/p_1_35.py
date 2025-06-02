import random


def birthday_paradox(n, num_trials):
    matches = 0
    for _ in range(num_trials):
        birthdays = set()
        found_duplicate = False
        for _ in range(n):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                found_duplicate = True
                break
            birthdays.add(birthday)
        if found_duplicate:
            matches += 1
    return matches / num_trials


print(birthday_paradox(23, 10))
