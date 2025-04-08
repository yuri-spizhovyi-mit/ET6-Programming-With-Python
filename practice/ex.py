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
        return self.scr

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
