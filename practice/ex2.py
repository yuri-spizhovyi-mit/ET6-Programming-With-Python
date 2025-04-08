from xlsxwriter.utility import re_trailing


class Node:
    """Class Node"""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return f"The name of the node is {self.name}"


a = Node("A")
print(a)
print(a.get_name())


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
        return self.src.get_name() + "->" + self.dest.get_name()


b = Node("B")
e = Edge(a, b)
print(e)


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return (
            self.src.get_name() + "->(" + str(self.weight) + ")" + self.dest.get_name()
        )


e1 = WeightedEdge(a, b, 5)
print(e1)


class Digraph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError("Duplicate node")
        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        result = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                result += src.get_name() + "->" + dest.get_name() + "\n"
        return result[:-1]


dg = Digraph()
a = Node("A")
b = Node("B")
dg.add_node(a)
dg.add_node(b)
e = Edge(a, b)
dg.add_edge(e)
print(dg)  # Output: A->B


class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)


g = Graph()
a = Node("A")
b = Node("B")
g.add_node(a)
g.add_node(b)
ge = Edge(a, b)
g.add_edge(ge)
print("Undirected Graph")
print(g)
