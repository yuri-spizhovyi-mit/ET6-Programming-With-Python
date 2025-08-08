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
#         A
#       /   \
#      B     C
#     / \   /  \
#    D   E G    F


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_iterative(root):
    if not root:
        return
    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val, end=" ")

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


tree = TreeNode("A")
tree.left = TreeNode("B")
tree.right = TreeNode("C")
tree.left.left = TreeNode("D")
tree.left.right = TreeNode("E")
tree.right.left = TreeNode("F")
tree.right.right = TreeNode("G")
preorder_iterative(tree)  # Expected output: A B D E C
