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


def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val, end="->")
    inorder(node.right)


node = TreeNode("A")
node.left = TreeNode("B")
node.right = TreeNode("C")
node.left.left = TreeNode("D")
node.left.right = TreeNode("E")
node.right.left = TreeNode("G")
node.right.right = TreeNode("F")
inorder(node)
