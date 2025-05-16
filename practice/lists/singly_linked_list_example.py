# singly_linked_list_example.py


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    # Real-world example: morning routine
    routine = SinglyLinkedList()
    routine.append("Wake up")
    routine.append("Brush teeth")
    routine.append("Drink water")
    routine.append("Exercise")
    routine.append("Eat breakfast")

    print("Morning Routine:")
    routine.print_list()
