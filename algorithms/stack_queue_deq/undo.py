undo_stack = []

# User types text
undo_stack.append("Hello")
undo_stack.append("Hello, world")

# User hits Undo
last_state = undo_stack.pop()
print("Reverted to:", last_state)
