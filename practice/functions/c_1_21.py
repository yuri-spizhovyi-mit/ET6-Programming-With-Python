def read_and_reverse_lines():
    lines = []
    print("Enter text (Ctrl+D to end input):")
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        print("\nReversed lines:")
        for line in reversed(lines):
            print(line)


if __name__ == "__main__":
    read_and_reverse_lines()
