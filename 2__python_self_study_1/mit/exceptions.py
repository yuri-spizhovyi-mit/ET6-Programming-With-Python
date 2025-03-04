try:
    a = int(input("A: "))
    b = int(input("B: "))
    print(a / b)
    print("Okay")
except ValueError:
    print("Could not convert to a number")
except ZeroDivisionError:
    print("Bug in user input")
print("Outside")
