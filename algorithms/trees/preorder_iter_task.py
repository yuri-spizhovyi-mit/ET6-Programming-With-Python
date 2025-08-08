class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder_iterative(root):
    if not root:
        return
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so left is processed first

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


# Build the tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(preorder_iterative(root))  # Should print [1, 2, 4, 5, 3]
