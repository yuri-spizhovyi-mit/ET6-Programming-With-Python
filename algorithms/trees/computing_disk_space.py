class FileSystemNode:
    def __init__(self, name, size=0, is_file=False):
        self.name = name
        self.size = size        # file size if is_file=True
        self.is_file = is_file
        self.children = []      # only used if it's a folder

    def add_child(self, child):
        if not self.is_file:
            self.children.append(child)
