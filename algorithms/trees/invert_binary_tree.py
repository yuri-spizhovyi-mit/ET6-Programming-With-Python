class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    root.left, root.right = (
        invert_binary_tree(root.right),
        invert_binary_tree(root.left),
    )
    return root


# Tree: [3, 9, 20, None, None, 15, 7]

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

inverted_tree = invert_binary_tree(tree)
print(inverted_tree.left.left.val)
