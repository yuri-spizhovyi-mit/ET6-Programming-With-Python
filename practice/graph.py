class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name + "A"


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
