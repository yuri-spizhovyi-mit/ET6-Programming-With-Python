from graph_classes import Graph, Digraph, Edge, Node


def dfs(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                new_path = dfs(graph, node, end, path, shortest, toPrint)
                if new_path is not None:
                    shortest = new_path

    return shortest


def shortest(graph, start, end, toPrint=False):
    return dfs(graph, start, end, [], None, toPrint)


def buildCityGraph(graphType):
    g = graphType()
    for name in (
        "Boston",
        "Providence",
        "New York",
        "Chicago",
        "Denver",
        "Phoenix",
        "Los Angeles",
    ):  # Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode("Boston"), g.getNode("Providence")))
    g.addEdge(Edge(g.getNode("Boston"), g.getNode("New York")))
    g.addEdge(Edge(g.getNode("Providence"), g.getNode("Boston")))
    g.addEdge(Edge(g.getNode("Providence"), g.getNode("New York")))
    g.addEdge(Edge(g.getNode("New York"), g.getNode("Chicago")))
    g.addEdge(Edge(g.getNode("Chicago"), g.getNode("Phoenix")))
    g.addEdge(Edge(g.getNode("Chicago"), g.getNode("Denver")))
    g.addEdge(Edge(g.getNode("Denver"), g.getNode("Phoenix")))
    g.addEdge(Edge(g.getNode("Denver"), g.getNode("New York")))
    g.addEdge(Edge(g.getNode("Los Angeles"), g.getNode("Boston")))
    return g


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + "->"
    return result


def runSP(source, destination):
    gr = buildCityGraph(Digraph)
    sp = shortest(gr, gr.getNode(source), gr.getNode(destination), toPrint=True)
    if sp is not None:
        print("Shortest path from", source, "to", destination, "is", printPath(sp))
    else:
        print("There is no path from", source, "to", destination)


# testSP('Chicago', 'Boston')
runSP("Boston", "Phoenix")
