class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    # Map each value to its index in inorder for O(1) lookups
    in_index_map = {val: idx for idx, val in enumerate(inorder)}

    def array_to_tree(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right or in_left > in_right:
            return None

        # The first value in preorder is the root
        root_val = preorder[pre_left]
        root = TreeNode(root_val)

        # Find the root in inorder
        root_index_in_inorder = in_index_map[root_val]

        # Number of nodes in left subtree
        left_subtree_size = root_index_in_inorder - in_left

        # Build left subtree
        root.left = array_to_tree(
            pre_left + 1,
            pre_left + left_subtree_size,
            in_left,
            root_index_in_inorder - 1,
        )

        # Build right subtree
        root.right = array_to_tree(
            pre_left + left_subtree_size + 1,
            pre_right,
            root_index_in_inorder + 1,
            in_right,
        )

        return root

    return array_to_tree(0, len(preorder) - 1, 0, len(inorder) - 1)


# Example input
preorder = [3, 5, 6, 2, 7, 4, 1, 0, 8]
inorder = [6, 5, 7, 2, 4, 3, 0, 1, 8]

root = buildTree(preorder, inorder)

# Helper function: level-order print
from collections import deque


def level_order(root):
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        res.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    # Trim trailing None values
    while res and res[-1] is None:
        res.pop()
    return res


print(level_order(root))
# Output: [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
