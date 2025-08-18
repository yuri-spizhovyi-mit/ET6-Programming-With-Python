class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class EulerTour:
    def __init__(self, root):
        self.root = root

    def tour(self, node, depth=0, path=[]):
        """Perform Euler Tour starting from a given node"""
        if node is None:
            return

        # 1. Pre-visit (before left child)
        self.pre_visit(node, depth, path)

        # Go left
        if node.left:
            path.append(0)  # going left
            self.tour(node.left, depth + 1, path)
            path.pop()

        # 2. In-visit (between left and right)
        self.in_visit(node, depth, path)

        # Go right
        if node.right:
            path.append(1)  # going right
            self.tour(node.right, depth + 1, path)
            path.pop()

        # 3. Post-visit (after right child)
        self.post_visit(node, depth, path)

    # Hooks (can be castomized)
    def pre_visit(self, node, depth, path):
        pass

    def in_visit(self, node, depth, path):
        pass

    def post_visit(self, node, depth, path):
        pass


class Traversals(EulerTour):
    def __init__(self, root):
        super().__init__(root)
        self.preorder = []
        self.inorder = []
        self.postorder = []

    def pre_visit(self, node, depth, path):
        self.preorder.append(node.value)

    def in_visit(self, node, depth, path):
        self.inorder.append(node.value)

    def post_visit(self, node, depth, path):
        self.postorder.append(node.value)
