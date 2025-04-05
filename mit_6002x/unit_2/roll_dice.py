import random


def rollDie():
    """Returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])


def rollN(n):
    result = ""
    for i in range(n):
        result = result + str(rollDie())
    return result

count = 0
amount = []
for i in range(500):
    result = rollN(2)
    print(result)
    if int(result) == 11:
      count += 1
      amount.append(result)
print(count, amount)  
