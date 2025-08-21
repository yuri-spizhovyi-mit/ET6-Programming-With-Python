class FileSystemNode:
    def __init__(self, name, size=0, is_file=False):
        self.name = name
        self.size = size  # file size if is_file=True
        self.is_file = is_file
        self.children = []  # only used if it's a folder

    def add_child(self, child):
        if not self.is_file:
            self.children.append(child)


def compute_disk_space(node):
    """Return total disk space used by the subtree rooted at node."""
    if node.is_file:
        return node.size

    total = 0
    for child in node.children:
        total += compute_disk_space(child)
    return total


# Build example tree
root = FileSystemNode("root")  # folder
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

# Compute total disk usage
print("Total disk space used:", compute_disk_space(root), "KB")
