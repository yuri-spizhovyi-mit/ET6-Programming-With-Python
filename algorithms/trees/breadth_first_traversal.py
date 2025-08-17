from collections import deque


#       A
#      / \
#     B   C
#    / \
#   D   E


class Tree:
    """Simple general tree structure with BFS traversal."""

    class Node:
        def __init__(self, value):
            self.value = value
            self.children = []

    def __init__(self, root=None):
        self._root = root

    def root(self):
        return self._root

    def is_empty(self):
        return self._root is None

    def children(self, node):
        return node.children

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            fringe = deque()  # queue of nodes
            fringe.append(self.root())  # start with root
            while fringe:
                p = fringe.popleft()  # remove from front of the queue
                yield p  # visit node
                for c in self.children(p):
                    fringe.append(c)  # add children to back of queue


# Build the tree
root = Tree.Node("A")
b = Tree.Node("B")
c = Tree.Node("C")
d = Tree.Node("D")
e = Tree.Node("E")
f = Tree.Node("F")

root.children = [b, c, d]
b.children = [e, f]

tree = Tree(root)

# BFS Traversal
print("Breadth-First Traversal:")
for node in tree.breadthfirst():
    print(node.value, end=" ")
