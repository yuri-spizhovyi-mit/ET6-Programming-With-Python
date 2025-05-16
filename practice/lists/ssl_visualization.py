import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.nodes = []  # For visualization

    def append(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)  # Keep track for visualization
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def visualize(self):
        fig, ax = plt.subplots(figsize=(len(self.nodes) * 2, 2))
        ax.set_xlim(0, len(self.nodes) * 2)
        ax.set_ylim(-1, 1)
        ax.axis("off")

        for i, node in enumerate(self.nodes):
            x = i * 2
            # Draw node as a circle
            circle = plt.Circle((x, 0), 0.5, color="skyblue", ec="black")
            ax.add_patch(circle)
            ax.text(
                x,
                0,
                str(node.value),
                ha="center",
                va="center",
                fontsize=12,
                weight="bold",
            )

            # Draw arrow to next node
            if i < len(self.nodes) - 1:
                ax.annotate(
                    "",
                    xy=(x + 1.0, 0),
                    xytext=(x + 0.5, 0),
                    arrowprops=dict(arrowstyle="->", lw=2),
                )

        plt.title("Singly Linked List Visualization", fontsize=14)
        plt.show()


# Example usage
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.visualize()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
node3.next = None  # This is the last node

print(id(node1))  # Address of node1
print(id(node1.next))  # Should match address of node2
print(id(node2.next))  # Should match address of node3
