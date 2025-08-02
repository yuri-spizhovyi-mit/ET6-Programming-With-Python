class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Insert a value into the binary tree (complete binary tree insertion)"""
        if not self.root:
            self.root = TreeNode(val)
            return

        from collections import deque

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if not node.left:
                node.left = TreeNode(val)
                return
            if not node.right:
                node.right = TreeNode(val)
                return
            queue.append(node.left)
            queue.append(node.right)

    def search(self, val):
        """Search for a value in the binary tree using BFS"""
        if not self.root:
            return False

        from collections import deque

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.val == val:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def inorder_traversal(self):
        """Inorder traversal: left -> root -> right"""
        return self._inorder_helper(self.root)

    def _inorder_helper(self, node):
        if not node:
            return []
        return (
            self._inorder_helper(node.left)
            + [node.val]
            + self._inorder_helper(node.right)
        )

    def preorder_traversal(self):
        """Preorder traversal: root -> left -> right"""
        return self._preorder_helper(self.root)

    def _preorder_helper(self, node):
        if not node:
            return []
        return (
            [node.val]
            + self._preorder_helper(node.left)
            + self._preorder_helper(node.right)
        )

    def postorder_traversal(self):
        """Postorder traversal: left -> right -> root"""
        return self._postorder_helper(self.root)

    def _postorder_helper(self, node):
        if not node:
            return []
        return (
            self._postorder_helper(node.left)
            + self._postorder_helper(node.right)
            + [node.val]
        )

    def level_order_traversal(self):
        """Level order traversal (BFS)"""
        if not self.root:
            return []

        from collections import deque

        queue = deque([self.root])
        result = []

        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result

    def get_height(self):
        """Get the height of the tree"""
        return self._get_height_helper(self.root)

    def _get_height_helper(self, node):
        if not node:
            return 0
        left = self._get_height_helper(node.left)
        right = self._get_height_helper(node.right)
        return max(left, right) + 1

    def count_nodes(self):
        """Count the total number of nodes in the tree"""
        return self._count_nodes_helper(self.root)

    def _count_nodes_helper(self, node):
        if not node:
            return 0
        return (
            1
            + self._count_nodes_helper(node.left)
            + self._count_nodes_helper(node.right)
        )


# Example usage and testing
if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree()

    # Insert some values
    values = [1, 2, 3, 4, 5, 6, 7]
    for number in values:
        tree.insert(number)

    print("Binary Tree Example")
    print("=" * 50)

    # Test search functionality
    print(f"Search for 5: {tree.search(5)}")  # True
    print(f"Search for 10: {tree.search(10)}")  # False

    # Test different traversal methods
    print(f"\nInorder traversal: {tree.inorder_traversal()}")
    print(f"Preorder traversal: {tree.preorder_traversal()}")
    print(f"Postorder traversal: {tree.postorder_traversal()}")
    print(f"Level order traversal: {tree.level_order_traversal()}")

    # Test tree properties
    print(f"\nTree height: {tree.get_height()}")
    print(f"Total nodes: {tree.count_nodes()}")

    # Visual representation of the tree
    print("\nTree structure:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\ / \\")
    print("   4  5 6  7")
