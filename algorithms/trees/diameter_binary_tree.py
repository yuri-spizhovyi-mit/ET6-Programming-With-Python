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


# Build the test tree:
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

# Run the function
print("Diameter of the binary tree:", diameterOfBinaryTree(root))
