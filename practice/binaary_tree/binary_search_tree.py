class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = Node(new_value)
            else:
                self.left.insert(new_value)
        else:
            if self.right is None:
                self.right = Node(new_value)
            else:
                self.right.insert(new_value)


# Create root node
root = Node(10)

# Insert values
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(7)
root.insert(20)
root.insert(50)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)


inorder(root)  # Output: 2 5 7 10 15 20 50
