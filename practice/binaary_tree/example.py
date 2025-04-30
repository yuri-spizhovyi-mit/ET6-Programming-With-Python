class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)

# Add children to left node
root.left.left = Node(2)
root.left.right = Node(7)

# Add child to right node
root.right.right = Node(20)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)


inorder(root)
