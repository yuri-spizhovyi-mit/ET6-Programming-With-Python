x = 27
epsilon = 0.5
num_guesses = 0
low = 0
high = x
ans = (high + low) / 2

while abs(ans**3 - x) >= epsilon:
    print(f"low = {low} high = {high} ans = {ans}")
    num_guesses += 1
    if abs(ans**3) < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print(f"num_guesses = {num_guesses}")
print(f"{ans} is close to cube root of {x}")
