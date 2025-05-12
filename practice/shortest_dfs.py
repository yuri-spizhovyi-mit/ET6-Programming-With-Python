from collections import deque

graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}


def bfs(graph, start):
    visited = set()
    visited_printed = ''
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            visited_printed += node + "->"
            for neighbor in graph[node]:
                queue.append(neighbor)
    return visited_printed[:-2]


# print(bfs(graph, "C"))


def dfs(graph, node, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if node not in visited:
        visited.add(node)
        path.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited, path)

    return path


result = dfs(graph, "C", None)
print("->".join(result))
