def dfs(digraph, start, end, path, shortest):
    path = path + [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None of len(path) < len(shortest):
                pass
