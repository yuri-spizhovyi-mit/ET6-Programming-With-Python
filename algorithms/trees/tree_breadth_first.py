from collections import deque


class LinkedBinaryTree:
    class Node:
        def __init__(self, element, left=None, right=None):
            self.element = element
            self.left = left
            self.right = right

    def __init__(self, root=None):
        self._root = root
        self._default_traversal = "inorder"

    def root(self):
        return self._root

    def is_empty(self):
        return self._root is None

    # (iterators + pretty_print already included above...)

    # ---------------------------------------
    # Pretty Print (BFS Folder-like Listing)
    # ---------------------------------------

    def pretty_print(self, node=None, prefix="", is_left=True):
        """Print tree structure in a pretty Euler-style sideways format."""
        if node is None:
            node = self._root

        if node.right:
            new_prefix = prefix + ("│   " if is_left else "    ")
            self.pretty_print(node.right, new_prefix, False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.element))

        if node.left:
            new_prefix = prefix + ("    " if is_left else "│   ")
            self.pretty_print(node.left, new_prefix, True)

    def pretty_print_bfs(self):
        """Print tree in BFS order like a folder structure."""
        if self.is_empty():
            print("(empty tree)")
            return

        queue = deque([(self._root, 0)])  # (node, depth)
        prev_depth = 0

        while queue:
            node, depth = queue.popleft()

            indent = "    " * depth
            if depth > prev_depth:
                print()
                prev_depth = depth

            print(f"{indent}- {node.element}")

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


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

print("Pretty Print (Euler-style):")
tree.pretty_print()

print("\nPretty Print (BFS Folder-like):")
tree.pretty_print_bfs()
