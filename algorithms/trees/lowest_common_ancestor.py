class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    if not root or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# Build the example tree
n3 = TreeNode(3)
n5 = TreeNode(5)
n1 = TreeNode(1)
n6 = TreeNode(6)
n2 = TreeNode(2)
n0 = TreeNode(0)
n8 = TreeNode(8)
n7 = TreeNode(7)
n4 = TreeNode(4)

n3.left, n3.right = n5, n1
n5.left, n5.right = n6, n2
n1.left, n1.right = n0, n8
n2.left, n2.right = n7, n4

print(lowest_common_ancestor(n3, n5, n1).val)  # 3
print(lowest_common_ancestor(n3, n5, n4).val)  # 5
