from collections import deque

graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}


def bfs(graph, start):
    # Step 1. Declare visited empty set
    visited = set()
    visited_print = ""
    # Step 2. Declare a queue with a start node
    queue = deque([start])

    # Step 3. Start while loop until queue is not empty

    while queue:
        # Step 4. Grab first node from the queue

        node = queue.popleft()
        # Check if node not in visited
        if node not in visited:
            visited.add(node)
            visited_print += node + "->"
            for neighbor in graph[node]:
                queue.append(neighbor)
    return visited_print[:-2]


print(bfs(graph, "C"))
