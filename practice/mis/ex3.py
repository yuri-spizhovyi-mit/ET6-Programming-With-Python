graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


dfs(graph, "A")
