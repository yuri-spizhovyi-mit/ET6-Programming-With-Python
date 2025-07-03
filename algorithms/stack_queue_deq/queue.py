from collections import deque

queue = deque()

# Customers arrive
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

# Serve first
print("Serving:", queue.popleft())  # Alice
