def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Example graph as an adjacency list
graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": ["B"]}

dfs(graph, "A")
