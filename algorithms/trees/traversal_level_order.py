"""
Preorder (Root → Left → Right)

🔹 1. Depth-First Traversal (DFS)
Explore as far down a branch as possible before backtracking.

Type	Order	Example Use
Inorder	Left → Root → Right	Binary Search Tree (returns sorted values)
Preorder	Root → Left → Right	Serialize tree, copy tree structure
Postorder	Left → Right → Root	Delete tree, evaluate expression tree
"""

# Inorder tree traversal
#        A
#       / \
#      B   C
#     / \   / \
#    D   E F    G
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(tree):
    if not tree:
        return
    queue = deque([tree])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


tree = TreeNode("A")
tree.left = TreeNode("B")
tree.right = TreeNode("C")
tree.left.left = TreeNode("D")
tree.left.right = TreeNode("E")
tree.right.left = TreeNode("F")
tree.right.right = TreeNode("G")
level_order(tree)  # Expected output: A B D E C
