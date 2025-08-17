from collections import deque


class BinaryTree:
    """A simple binary tree with multiple traversal methods."""

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

    # ----------------------------
    # Breadth-First Traversal (BFS)
    # ----------------------------
    def breadthfirst(self):
        """Level-order traversal using a queue."""
        if not self.is_empty():
            queue = deque()
            queue.append(self.root())
            while queue:
                node = queue.popleft()
                yield node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    # ----------------------------
    # Inorder Traversal
    # ----------------------------
    def inorder(self):
        """Left -> Root -> Right (recursive)."""
        if not self.is_empty():
            yield from self._subtree_inorder(self.root())

    def _subtree_inorder(self, node):
        if node.left:
            yield from self._subtree_inorder(node.left)
        yield node
        if node.right:
            yield from self._subtree_inorder(node.right)

    # ----------------------------
    # Preorder Traversal
    # ----------------------------
    def preorder(self):
        """Root -> Left -> Right (recursive)."""
        if not self.is_empty():
            yield from self._subtree_preorder(self.root())

    def _subtree_preorder(self, node):
        yield node
        if node.left:
            yield from self._subtree_preorder(node.left)
        if node.right:
            yield from self._subtree_preorder(node.right)

    # ----------------------------
    # Postorder Traversal
    # ----------------------------
    def postorder(self):
        """Left -> Right -> Root (recursive)."""
        if not self.is_empty():
            yield from self._subtree_postorder(self.root())

    def _subtree_postorder(self, node):
        if node.left:
            yield from self._subtree_postorder(node.left)
        if node.right:
            yield from self._subtree_postorder(node.right)
        yield node


# Build the binary tree
root = BinaryTree.Node("A")
root.left = BinaryTree.Node("B")
root.right = BinaryTree.Node("C")
root.left.left = BinaryTree.Node("D")
root.left.right = BinaryTree.Node("E")
root.right.right = BinaryTree.Node("F")

tree = BinaryTree(root)

# BFS
print("BFS:", [node.value for node in tree.breadthfirst()])

# Inorder
print("Inorder:", [node.value for node in tree.inorder()])

# Preorder
print("Preorder:", [node.value for node in tree.preorder()])

# Postorder
print("Postorder:", [node.value for node in tree.postorder()])
