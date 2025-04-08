class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


a = Node("A")
print(a)  # Output: A
print(a.getName())  # Output: A
