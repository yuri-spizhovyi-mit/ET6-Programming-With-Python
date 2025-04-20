class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


# a = Node("A")
# print(a)  # Output: A
# print(a.getName())  # Output: A


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + "->" + self.dest.getName()


a = Node("A")
b = Node("B")
e = Edge(a, b)
print(e)


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + "->(" + str(self.weight) + ")" + self.dest.getName()


e = WeightedEdge(a, b, 5)
print(e)  # Output: A->(5)B


class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError("Duplicate node")
        self.nodes.append(node)
        self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                result += src.getName() + "->" + dest.getName() + "\n"
        return result[:-1]  # Remove the last newline


g1 = Digraph()
a = Node("A")
b = Node("B")
g1.addNode(a)
g1.addNode(b)
e = Edge(a, b)
g1.addEdge(e)
print(g1)  # Output: A->B


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


g2 = Graph()
a = Node("A")
b = Node("B")
g2.addNode(a)
g2.addNode(b)
e = Edge(a, b)
g2.addEdge(e)
print(g2)
# Output:
# A->B
# B->A
