class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

        # if key == node.key, we ignore (no duplicates)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder(node.left)
        print(node.key, end=" ")
        if node.right:
            self.inorder(node.right)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1: no children
            if node.left is None and node.right is None:
                return None
            # Case 2: one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: two children
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


bst = BST()
for x in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(x)

print("Inorder (sorted):", end=" ")
bst.inorder()
print()

print("Search 40:", bst.search(40))
print("Search 90:", bst.search(90))

bst.delete(20)  # leaf
bst.delete(30)  # one child
bst.delete(50)  # two children

print("Inorder after deletions:", end=" ")
bst.inorder()
