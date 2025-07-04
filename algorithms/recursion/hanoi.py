def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disc 1 from {source} to {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        print(f"Move disc {n} from {source} to {target}")
        hanoi(n - 1, auxiliary, target, source)


hanoi(3, "A", "B", "C")
