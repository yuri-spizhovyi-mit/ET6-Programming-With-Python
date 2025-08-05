class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# Tree: [3, 9, 20, None, None, 15, 7]
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(max_depth(tree))  # Output: 3
