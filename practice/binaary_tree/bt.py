class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Step 1: Create any binary tree
root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)


def collect_values(node, values):
    if node:
        collect_values(node.left, values)
        values.append(node.value)
        collect_values(node.right, values)


values = []
collect_values(root, values)
print(values)  # ➜ [20, 30, 10, 15, 5]
values.sort()
print(values)  # ➜ [5, 10, 15, 20, 30]


def refill_tree(node, values_iter):
    if node:
        refill_tree(node.left, values_iter)
        node.value = next(values_iter)
        refill_tree(node.right, values_iter)


refill_tree(root, iter(values))


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)


inorder(root)  # Output: 5 10 15 20 30
