from collections import deque

def process_tasks(tasks):
    queue = deque(tasks)
    while queue:
        task = queue.popleft()
        print("Processing:", task)

# Test
process_tasks(["Download", "Scan", "Install"])
