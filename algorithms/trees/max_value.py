class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_max_value(root):
    if not root:
        return float("-inf")
    return max(root.val, find_max_value(root.left), find_max_value(root.right))


tree = TreeNode(-1)
tree.left = TreeNode(-2)
tree.left.left = TreeNode(-4)
tree.left.right = TreeNode(-50)
tree.right = TreeNode(-3)

print(find_max_value(tree))
