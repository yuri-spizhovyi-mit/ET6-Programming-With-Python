# Binary Tree Node Definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TASK 1: Maximum Depth of Binary Tree
# Problem: Find the maximum depth (height) of a binary tree
def max_depth(root):
    """
    Returns the maximum depth of a binary tree.

    Args:
        root: TreeNode - root of the binary tree

    Returns:
        int - maximum depth of the tree
    """
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1


# TASK 2: Invert Binary Tree
# Problem: Invert a binary tree (mirror it)
def invert_tree(root):
    """
    Inverts a binary tree by swapping left and right children recursively.

    Args:
        root: TreeNode - root of the binary tree

    Returns:
        TreeNode - root of the inverted tree
    """
    if not root:
        return None

    # Swap the left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert the subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


# TASK 3: Binary Tree Level Order Traversal
# Problem: Return level order traversal of binary tree nodes' values
def level_order(root):
    """
    Performs level order traversal (BFS) of a binary tree.

    Args:
        root: TreeNode - root of the binary tree

    Returns:
        List[List[int]] - list of lists containing values at each level
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


# TASK 4: Validate Binary Search Tree
# Problem: Check if a binary tree is a valid BST
def is_valid_bst(root):
    """
    Validates if a binary tree is a valid Binary Search Tree.

    Args:
        root: TreeNode - root of the binary tree

    Returns:
        bool - True if valid BST, False otherwise
    """

    def validate(node, min_val, max_val):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return validate(node.left, min_val, node.val) and validate(
            node.right, node.val, max_val
        )

    return validate(root, float("-inf"), float("inf"))


# TASK 5: Path Sum
# Problem: Check if there exists a root-to-leaf path with given sum
def has_path_sum(root, target_sum):
    """
    Checks if there exists a root-to-leaf path with sum equal to target_sum.

    Args:
        root: TreeNode - root of the binary tree
        target_sum: int - target sum to find

    Returns:
        bool - True if such path exists, False otherwise
    """
    if not root:
        return False

    # If it's a leaf node
    if not root.left and not root.right:
        return root.val == target_sum

    # Recursively check left and right subtrees with updated sum
    remaining_sum = target_sum - root.val
    return has_path_sum(root.left, remaining_sum) or has_path_sum(
        root.right, remaining_sum
    )


# Helper function to create a sample tree for testing
def create_sample_tree():
    """
    Creates a sample binary tree:
          3
         / \
        9   20
           /  \
          15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


# Example usage and testing
if __name__ == "__main__":
    # Create sample tree
    root = create_sample_tree()

    # Test Task 1: Maximum Depth
    print("Task 1 - Maximum Depth:")
    print(f"Max depth: {max_depth(root)}")  # Output: 3

    # Test Task 2: Invert Tree
    print("\nTask 2 - Invert Tree:")
    inverted_root = invert_tree(root)
    print("Tree inverted successfully")

    # Recreate tree for other tests (since we inverted it)
    root = create_sample_tree()

    # Test Task 3: Level Order Traversal
    print("\nTask 3 - Level Order Traversal:")
    levels = level_order(root)
    print(f"Levels: {levels}")  # Output: [[3], [9, 20], [15, 7]]

    # Test Task 4: Valid BST
    print("\nTask 4 - Valid BST:")
    print(f"Is valid BST: {is_valid_bst(root)}")  # Output: False

    # Create a valid BST for testing
    bst_root = TreeNode(5)
    bst_root.left = TreeNode(3)
    bst_root.right = TreeNode(7)
    bst_root.left.left = TreeNode(2)
    bst_root.left.right = TreeNode(4)
    print(f"Valid BST test: {is_valid_bst(bst_root)}")  # Output: True

    # Test Task 5: Path Sum
    print("\nTask 5 - Path Sum:")
    print(f"Has path sum 22: {has_path_sum(root, 22)}")  # Output: True (3->9)
    print(f"Has path sum 26: {has_path_sum(root, 26)}")  # Output: False
