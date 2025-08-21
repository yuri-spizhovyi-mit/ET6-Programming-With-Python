class FileSystemNode:
    def __init__(self, name, size=0, is_file=False):
        self.name = name
        self.size = size  # size if file
        self.is_file = is_file
        self.children = []  # only if folder

    def add_child(self, child):
        if not self.is_file:
            self.children.append(child)


class EulerTour:
    def __init__(self, root):
        self.root = root

    def tour(self, node):
        """Perform Euler Tour traversal."""
        if node is None:
            return None

        self.pre_visit(node)  # before children

        results = []
        for child in node.children:
            results.append(self.tour(child))

        answer = self.post_visit(node, results)  # after children
        return answer

    def pre_visit(self, node):
        pass

    def post_visit(self, node, results):
        pass


class DiskSpaceTour(EulerTour):
    def post_visit(self, node, results):
        """Compute disk space in postorder."""
        if node.is_file:
            return node.size
        else:
            total = sum(results)  # sum children’s sizes
            node.size = total  # update folder’s size
            return total


# Build sample file system
root = FileSystemNode("root")
docs = FileSystemNode("Documents")
pics = FileSystemNode("Pictures")

file1 = FileSystemNode("resume.pdf", size=120, is_file=True)
file2 = FileSystemNode("book.pdf", size=300, is_file=True)
file3 = FileSystemNode("photo1.jpg", size=500, is_file=True)
file4 = FileSystemNode("photo2.jpg", size=700, is_file=True)

# Build hierarchy
root.add_child(docs)
root.add_child(pics)

docs.add_child(file1)
docs.add_child(file2)

pics.add_child(file3)
pics.add_child(file4)

# Compute disk space with Euler Tour
tour = DiskSpaceTour(root)
total_space = tour.tour(root)

print("Total disk space used:", total_space, "KB")
print("Docs folder size:", docs.size, "KB")
print("Pics folder size:", pics.size, "KB")
