def is_balanced(expr):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

# Test
print(is_balanced("(a + b) * [c / d]"))  # True
print(is_balanced("((a + b]"))           # False
