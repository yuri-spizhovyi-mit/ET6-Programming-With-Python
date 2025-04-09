class Node:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


g1 = Node("A")
g2 = Node("B")
print(g1, g2)
print(g1.get_name())
print(g2.get_name())


class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.src + "->" + self.dest


e = Edge(g1.get_name(), g2.get_name())
print(e)


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.src + "->(" + str(self.weight) + ")" + self.dest


ew = WeightedEdge(g1.get_name(), g2.get_name(), 6)
print(ew)


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


g = Digraph()
c = Node("C")
d = Node("D")
g.add_node(c)
g.add_node(d)
ed = Edge(c, d)
g.add_edge(ed)
print(g)


class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)


g = Graph()
x = Node("X")
z = Node("Z")

g.add_node(x)
g.add_node(z)
edg = Edge(x, z)
g.add_edge(edg)
print(g)
