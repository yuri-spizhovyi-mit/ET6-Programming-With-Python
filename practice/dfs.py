from graph import Node, Edge, Digraph


def dfs_stack(graph, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            return path

        for neighbor in graph.childrenOf(current):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


# Set up graph
toronto = Node("Toronto")
montreal = Node("Montreal")
ottawa = Node("Ottawa")
quebec = Node("Quebec")

g = Digraph()
g.addNode(toronto)
g.addNode(montreal)
g.addNode(ottawa)
g.addNode(quebec)

g.addEdge(Edge(toronto, montreal))
g.addEdge(Edge(toronto, ottawa))
g.addEdge(Edge(montreal, quebec))
g.addEdge(Edge(ottawa, quebec))
g.addEdge(Edge(quebec, toronto))  # ← creates cycle

# Run DFS
path = dfs_stack(g, toronto, quebec)
if path:
    print("DFS Path:", " → ".join(node.getName() for node in path))
else:
    print("No path found.")
