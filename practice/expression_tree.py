class ExprNode:
    def __init__(self, value):
        self.value = value  # Can be an operator or a number
        self.left = None
        self.right = None


# Build: (3 + (4 * 5))
root = ExprNode("+")
root.left = ExprNode(3)
root.right = ExprNode("*")
root.right.left = ExprNode(4)
root.right.right = ExprNode(5)


def evaluate(node):
    if node is None:
        return 0
    if isinstance(node.value, int):  # Leaf node
        return node.value

    # Recursively evaluate left and right
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)

    # Apply the operator
    if node.value == "+":
        return left_val + right_val
    elif node.value == "-":
        return left_val - right_val
    elif node.value == "*":
        return left_val * right_val
    elif node.value == "/":
        return left_val / right_val


print(evaluate(root))  # Output: 23
