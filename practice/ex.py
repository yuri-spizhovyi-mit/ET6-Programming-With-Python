class Node:
    """Class Node"""

    def __init__(self, name):
        self.name = name

    def get_node(self):
        return self.name

    def __str__(self):
        return f"The name of the node is {self.name}"


a = Node("A")
print(a)
print(a.get_node())
