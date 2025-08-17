from collections import deque


class BinaryTree:
    """A simple binary tree with breadth-first traversal."""

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self, root=None):
        self._root = root

    def root(self):
        return self._root

    def is_empty(self):
        return self._root is None

    def breadthfirst(self):
        """Generate a breadth-first iteration of the tree nodes."""
        if not self.is_empty():
            queue = deque()
            queue.append(self.root())  # start with root
            while queue:
                node = queue.popleft()  # remove from front
                yield node  # visit this node
                if node.left is not None:
                    queue.append(node.left)  # enqueue left child
                if node.right is not None:
                    queue.append(node.right)  # enqueue right child


# Build the tree
root = BinaryTree.Node("A")
root.left = BinaryTree.Node("B")
root.right = BinaryTree.Node("C")
root.left.left = BinaryTree.Node("D")
root.left.right = BinaryTree.Node("E")
root.right.right = BinaryTree.Node("F")

tree = BinaryTree(root)

# BFS Traversal
print("Breadth-First Traversal:")
for node in tree.breadthfirst():
    print(node.value, end=" ")
