import random


# You are given this function - do not modify
def createRandomGraph():
    """Creates a digraph with 7 randomly chosen integer nodes from 0 to 9 and
    randomly chosen directed edges (between 10 and 20 edges)
    """
    g = {}
    n = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7)
    for i in n:
        g[i] = []
    edges = random.randint(10, 20)
    count = 0
    while count < edges:
        a = random.choice(n)
        b = random.choice(n)
        if b not in g[a] and a != b:
            g[a].append(b)
            count += 1
    return g


graph = {
    5: [4, 0, 8],
    0: [8, 5],
    8: [9, 2, 10],
    4: [6, 9, 5],
    6: [2, 4, 0],
    9: [5],
    2: [6, 8, 4, 0],
    10: [6],
}


# You are given this function - do not modify
def findPath(g, start, end, path=[]):
    """Uses DFS to find a path between a start and an end node in g.
    If no path is found, returns None. If a path is found, returns the
    list of nodes"""
    path = path + [start]
    if start == end:
        return path
    if not start in g:
        return None
    for node in g[start]:
        if node not in path:
            newpath = findPath(g, node, end, path)
            if newpath:
                return newpath
    return None


print(findPath(graph, 5, 2))


#########################
## WRITE THIS FUNCTION ##
#########################


def allReachable(g, n):
    """
    Assumes g is a directed graph and n a node in g.
    Returns a sorted list (increasing by node number) containing all
    nodes m such that there is a path from n to m in g.
    Does not include the node itself.
    """

    list_of_reachable_nodes = []
    for node in g:
        if node != n:
            if findPath(g, n, node) != None:
                list_of_reachable_nodes.append(node)
    return sorted(list_of_reachable_nodes)


print(allReachable(graph, 5))
