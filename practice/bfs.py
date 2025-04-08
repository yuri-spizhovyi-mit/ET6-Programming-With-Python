from graph import Node, WeightedEdge, Graph  # ⬅️ import what you need

from collections import deque


def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node in visited:
            continue

        print("Visiting:", node.getName())
        visited.add(node)

        if node.getName() == goal.getName():
            print("🎯 Found goal!")
            return path

        for neighbor in graph.childrenOf(node):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

    print("🚫 No path found")
    return None


# Create nodes
toronto = Node("Toronto")
montreal = Node("Montreal")
ottawa = Node("Ottawa")
quebec = Node("Quebec")


# Create and populate graph
g = Graph()
g.addNode(toronto)
g.addNode(montreal)
g.addNode(ottawa)
g.addNode(quebec)

g.addEdge(WeightedEdge(toronto, montreal, 540))
g.addEdge(WeightedEdge(montreal, ottawa, 200))
g.addEdge(WeightedEdge(toronto, ottawa, 450))
g.addEdge(WeightedEdge(montreal, quebec, 250))

# Run BFS
path = bfs_shortest_path(g, toronto, quebec)
if path:
    print("Path found:", " → ".join(node.getName() for node in path))
