class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Build the tree
root = Node(10)
root.left = Node(20)  # ❌ 20 > 10 (not allowed in BST)
root.right = Node(5)  # ❌ 5 < 10 (not allowed in BST)
root = Node("+")
root.left = Node(3)
root.right = Node("*")
root.right.left = Node(4)
root.right.right = Node(5)
