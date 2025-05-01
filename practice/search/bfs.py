from collections import deque

graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": ["B"]}


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)


# Same graph as above
bfs(graph, "A")
