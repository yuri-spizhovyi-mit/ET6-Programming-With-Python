from collections import deque


class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


def build_tree(values):
    """Build a binary tree from a list (level-order)."""
    if not values:
        return None

    nodes = [None if val is None else BinaryTree.Node(val) for val in values]

    for i in range(len(values)):
        if nodes[i] is not None:  # only connect if the node exists
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(values):
                nodes[i].left = nodes[left_index]
            if right_index < len(values):
                nodes[i].right = nodes[right_index]

    return nodes[0]  # root


# Input list (level-order, use None for missing nodes)
values = ["A", "B", "C", "D", "E", None, "F"]

root = build_tree(values)


# Quick test: print BFS
def bfs(root):
    if not root:
        return []
    queue, result = deque([root]), []
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


print("BFS:", bfs(root))
