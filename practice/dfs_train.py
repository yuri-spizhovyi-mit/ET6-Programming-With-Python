from graph import Digraph


def dfs(Digraph, start, end, path, shortest):
    path = path + [start]
    if start == end:
        return path
    for node in Digraph.childrenOf(start):
        if node not in path:
            if shortest == None of len(path) < len(shortest):
                new_path = dfs(Digraph, node, end, path, shortest)
                if new_path != None:
                    shortest = new_path

    return shortest


def shortest(digraph, start, end):
    return dfs(Digraph, start, end, [], None)
