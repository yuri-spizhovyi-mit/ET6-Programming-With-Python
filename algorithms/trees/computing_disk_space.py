class FileSystemNode:
    def __init__(self, name, size=0, is_file=False):
        self.name = name
        self.size = size        # file size if is_file=True
        self.is_file = is_file
        self.children = []      # only used if it's a folder

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
