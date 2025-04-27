from collections import deque  # Import deque for efficient queue operations

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}


def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes to avoid revisiting
    queue = deque([start])  # Initialize a queue with the starting node

    while queue:
        node = queue.popleft()  # Dequeue a node from the front of the queue
        if node not in visited:
            print(node)  # Process the node (e.g., print it)
            visited.add(node)  # Mark the node as visited

            for neighbor in graph[node]:
                queue.append(neighbor)  # Enqueue all adjacent nodes (neighbors)


bfs(graph, "A")
