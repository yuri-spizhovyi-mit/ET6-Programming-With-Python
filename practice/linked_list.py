# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Head of the list

    # Add element at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Print all elements
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()
