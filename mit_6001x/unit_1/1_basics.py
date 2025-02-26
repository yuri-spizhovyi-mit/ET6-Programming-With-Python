def conditionals(x):
    if x % 2 == 0:
        if x % 3 == 0:
            print(f"{x} Divisible by 2 and 3")
        else:
            print(f"{x} Divisible by 2 and not by 3")
    elif x % 3 == 0:
        print(f"{x} Divisible by 3 but not by 2")
    else:
        print(f"{x} Not divisible by 3 and 2")


conditionals(2)
conditionals(3)
conditionals(12)
conditionals(7)
# asdfasdfasf
