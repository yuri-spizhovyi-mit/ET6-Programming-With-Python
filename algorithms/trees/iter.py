from collections import deque


class LinkedBinaryTree:
    """Binary tree with explicit traversal iterators (no yield)."""

    class Node:
        def __init__(self, element, left=None, right=None):
            self.element = element
            self.left = left
            self.right = right

    def __init__(self, root=None):
        self._root = root
        self._default_traversal = "inorder"  # default iteration order

    def root(self):
        return self._root

    def is_empty(self):
        return self._root is None

    # --------------------------------------------------
    # Default Python iteration
    # --------------------------------------------------
    def __iter__(self):
        """Default iteration over elements (not nodes)."""
        if self._default_traversal == "inorder":
            return (node.element for node in self.inorder())
        elif self._default_traversal == "preorder":
            return (node.element for node in self.preorder())
        elif self._default_traversal == "postorder":
            return (node.element for node in self.postorder())
        elif self._default_traversal == "breadthfirst":
            return (node.element for node in self.breadthfirst())
        else:
            raise ValueError(f"Unknown traversal: {self._default_traversal}")

    def set_default(self, traversal):
        """Change default iteration order."""
        if traversal not in {"inorder", "preorder", "postorder", "breadthfirst"}:
            raise ValueError(
                "Traversal must be one of inorder, preorder, postorder, breadthfirst"
            )
        self._default_traversal = traversal

    # -----------------------------
    # Preorder Traversal Iterator
    # -----------------------------
    def preorder(self):
        return self.PreorderIterator(self)

    class PreorderIterator:
        def __init__(self, tree):
            self._snapshot = []
            if not tree.is_empty():
                self._preorder(tree.root())
            self._index = 0

        def _preorder(self, node):
            if node:
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
            raise StopIteration

    # -----------------------------
    # Inorder Traversal Iterator
    # -----------------------------
    def inorder(self):
        return self.InorderIterator(self)

    def pretty_print(self, node=None, prefix="", is_left=True):
        """Print tree structure in a pretty format like `tree` command."""
        if node is None:
            node = self._root

        if node.right:
            new_prefix = prefix + ("│   " if is_left else "    ")
            self.pretty_print(node.right, new_prefix, False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.element))

        if node.left:
            new_prefix = prefix + ("    " if is_left else "│   ")
            self.pretty_print(node.left, new_prefix, True)

    class InorderIterator:
        def __init__(self, tree):
            self._snapshot = []
            if not tree.is_empty():
                self._inorder(tree.root())
            self._index = 0

        def _inorder(self, node):
            if node:
                self._inorder(node.left)
                self._snapshot.append(node)
                self._inorder(node.right)

        def __iter__(self):
            return self

        def __next__(self):
            if self._index < len(self._snapshot):
                node = self._snapshot[self._index]
                self._index += 1
                return node
            raise StopIteration

    # -----------------------------
    # Postorder Traversal Iterator
    # -----------------------------
    def postorder(self):
        return self.PostorderIterator(self)

    class PostorderIterator:
        def __init__(self, tree):
            self._snapshot = []
            if not tree.is_empty():
                self._postorder(tree.root())
            self._index = 0

        def _postorder(self, node):
            if node:
                self._postorder(node.left)
                self._postorder(node.right)
                self._snapshot.append(node)

        def __iter__(self):
            return self

        def __next__(self):
            if self._index < len(self._snapshot):
                node = self._snapshot[self._index]
                self._index += 1
                return node
            raise StopIteration

    # -----------------------------
    # Breadth-First Traversal Iterator
    # -----------------------------
    def breadthfirst(self):
        return self.BreadthFirstIterator(self)

    class BreadthFirstIterator:
        def __init__(self, tree):
            self._snapshot = []
            if not tree.is_empty():
                self._bfs(tree.root())
            self._index = 0

        def _bfs(self, root):
            queue = deque([root])
            while queue:
                node = queue.popleft()
                self._snapshot.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        def __iter__(self):
            return self

        def __next__(self):
            if self._index < len(self._snapshot):
                node = self._snapshot[self._index]
                self._index += 1
                return node
            raise StopIteration


# Build sample tree:
#        A
#       / \
#      B   C
#     / \
#    D   E

root = LinkedBinaryTree.Node("A")
root.left = LinkedBinaryTree.Node("B")
root.right = LinkedBinaryTree.Node("C")
root.left.left = LinkedBinaryTree.Node("D")
root.left.right = LinkedBinaryTree.Node("E")

tree = LinkedBinaryTree(root)

print("Tree structure:")
tree.pretty_print()

print("Preorder:", [n.element for n in tree.preorder()])
print("Inorder:", [n.element for n in tree.inorder()])
print("Postorder:", [n.element for n in tree.postorder()])
print("Breadth-First:", [n.element for n in tree.breadthfirst()])

# Default iteration is inorder
print("Default (inorder):", [x for x in tree])

# Change default traversal
tree.set_default("preorder")
print("Default (preorder):", [x for x in tree])

tree.set_default("postorder")
print("Default (postorder):", [x for x in tree])

tree.set_default("breadthfirst")
print("Default (breadthfirst):", [x for x in tree])
