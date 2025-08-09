class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)


def has_path_sum(root, target_sum):
    if not root:
        return False

    # if it's a leaf node, check if the sum matches

    if not root.left and not root.right:
        return target_sum == root.val

    # Recurse on left and right with reduced target_sum
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(
        root.right, target_sum - root.val
    )


print(has_path_sum(root, 22))  # Expected: True
