import heapq


class Node:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class WeightedEdge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def getWeight(self):
        return self.weight

    def __str__(self):
        return f"{self.src}->{self.dest} ({self.weight})"


class WeightedGraph:
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicate node")
        self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        weight = edge.getWeight()
        if src not in self.edges or dest not in self.edges:
            raise ValueError("Node not in graph")
        self.edges[src].append((dest, weight))

    def childrenOf(self, node):
        return self.edges[node]


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.edges}
    distances[start] = 0
    priority_queue = [(0, start.getName(), start)]  # (distance, node)

    while priority_queue:
        current_distance, _, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue  # Already found a shorter path

        for neighbor, weight in graph.childrenOf(current_node):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor.getName(), neighbor))

    return distances


# Build graph
g = WeightedGraph()
for name in ["A", "B", "C", "D", "E"]:
    g.addNode(Node(name))

nodes = {name: Node(name) for name in ["A", "B", "C", "D", "E"]}
g.addEdge(WeightedEdge(nodes["A"], nodes["B"], 1))
g.addEdge(WeightedEdge(nodes["A"], nodes["C"], 4))
g.addEdge(WeightedEdge(nodes["B"], nodes["C"], 2))
g.addEdge(WeightedEdge(nodes["B"], nodes["D"], 5))
g.addEdge(WeightedEdge(nodes["C"], nodes["D"], 1))
g.addEdge(WeightedEdge(nodes["D"], nodes["E"], 3))

# Run Dijkstra
shortest = dijkstra(g, nodes["A"])

# Print distances
for node, dist in shortest.items():
    print(f"Distance from A to {node}: {dist}")
