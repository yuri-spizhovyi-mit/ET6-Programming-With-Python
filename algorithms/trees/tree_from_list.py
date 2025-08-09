from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree_from_list(values):
    if not values:
        return None

    # Create root
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1  # index in list

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


values = [1, 2, 3, 4, 5, None, 7]
root = build_tree_from_list(values)


# Let's check by doing level-order traversal
def level_order(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    return result


print(level_order(root))  # ✅ Output: [1, 2, 3, 4, 5, None, 7]
