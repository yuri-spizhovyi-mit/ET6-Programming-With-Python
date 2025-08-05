class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter = 0

    def dfs(node):
        nonlocal diameter
        if not node:
            return 0
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        # update the diameter at this node
        diameter = max(diameter, left_height + right_height)
        # return the height of the current node
        return max(left_height, right_height) + 1

    dfs(root)
    return diameter
