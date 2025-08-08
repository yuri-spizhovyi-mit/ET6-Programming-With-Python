"""
 Inorder Iterative (Left → Root → Right)

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
#    D   E G    F


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_iterative(root):
    stack = []
    current = root

    while current or stack:
        # Reach the leftmost node
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.val, end=" ")

        # Move to the right subtree
        current = current.right


node = TreeNode("A")
node.left = TreeNode("B")
node.right = TreeNode("C")
node.left.left = TreeNode("D")
node.left.right = TreeNode("E")
node.right.left = TreeNode("G")
node.right.right = TreeNode("F")
inorder_iterative(node)  # Expected output: D B E A C
