class ArrayBinaryTree:
    def __init__(self, capacity=20):
        self.tree = [None] * (capacity + 1)  # index 0 is unused
        self.size = 0

    def root(self):
        return self.tree[1] if self.size > 0 else None

    def parent(self, i):
        if i > 1 and self.tree[i] is not None:
            return self.tree[i // 2]
        return None

    def left(self, i):
        if 2 * i < len(self.tree):
            return self.tree[2 * i]
        return None

    def right(self, i):
        if 2 * i + 1 < len(self.tree):
            return self.tree[2 * i + 1]
        return None

    def insert(self, i, value):
        """Insert value at position i (you must choose index respecting rules)."""
        if i >= len(self.tree):
            raise IndexError("Index out of bounds")
        if self.tree[i] is None:
            self.size += 1
        self.tree[i] = value

    def preorder(self, i=1):
        if i < len(self.tree) and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i)
            self.preorder(2 * i + 1)

    def inorder(self, i=1):
        if i < len(self.tree) and self.tree[i] is not None:
            self.inorder(2 * i)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 1)

    def postorder(self, i=1):
        if i < len(self.tree) and self.tree[i] is not None:
            self.postorder(2 * i)
            self.postorder(2 * i + 1)
            print(self.tree[i], end=" ")


T = ArrayBinaryTree()
T.insert(1, "A")  # root
T.insert(2, "B")  # left child of A
T.insert(3, "C")  # right child of A
T.insert(4, "D")  # left child of B
T.insert(5, "E")  # right child of B

print("Preorder: ", end="")
T.preorder()  # A B D E C

print("\nInorder: ", end="")
T.inorder()  # D B E A C

print("\nPostorder: ", end="")
T.postorder()  # D E B C A
