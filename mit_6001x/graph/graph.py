class Node:
    """Class Node"""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge:
    """Class Edge"""

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return f"{self.src} -> {self.dest}"


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"{self.src.get_name()} -> ({self.weight}) {self.dest.get_name()}"


class Digraph:
    """Class Digraph"""

    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError("Duplicat node")
        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def child_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        result = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                result += f"{src.get_name()} -> {dest.get_name()} \n"
        return result[:-1]


class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)


node_Vancouver = Node("Vancouver")
print(node_Vancouver.get_name())
node_Quebec = Node("Quebec")
print((node_Quebec.get_name()))
node_Toronto = Node("Toronto")

edge_1 = Edge(node_Vancouver, node_Quebec)
edge_2 = Edge(node_Toronto, node_Quebec)
g = Digraph()
g.add_node(node_Toronto)
g.add_node(node_Quebec)
g.add_node(node_Vancouver)
g.add_edge(edge_1)
g.add_edge(edge_2)
print(g)
