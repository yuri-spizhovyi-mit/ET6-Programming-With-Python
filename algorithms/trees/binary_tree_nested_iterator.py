class LinkedBinaryTree:
    """Binary tree with explicit preorder iterator."""

    class Node:
        def __init__(self, element, left=None, right=None):
            self.element = element
            self.left = left
            self.right = right

    def __init__(self, root=None):
        self._root = root

    def root(self):
        return self._root

    def is_empty(self):
        return self._root is None

    # -----------------------------
    # Explicit Preorder Iterator
    # -----------------------------
    def preorder(self):
        return self.PreorderIterator(self)

    class PreorderIterator:
        def __init__(self, tree):
            self._snapshot = []
            if not tree.is_empty():
                self._preorder(tree.root())
            self._index = 0  # for iteration

        def _preorder(self, node):
            """Build snapshot list in preorder."""
            if node is not None:
                self._snapshot.append(node)
                self._preorder(node.left)
                self._preorder(node.right)

        def __iter__(self):
            return self

        def __next__(self):
            if self._index < len(self._snapshot):
                node = self._snapshot[self._index]
                self._index += 1
                return node
            else:
                raise StopIteration


# Build small tree:   A
#                    / \
#                   B   C
root = LinkedBinaryTree.Node("A")
root.left = LinkedBinaryTree.Node("B")
root.right = LinkedBinaryTree.Node("C")

tree = LinkedBinaryTree(root)

print("Preorder traversal:")
for node in tree.preorder():
    print(node.element, end=" ")
