class SinglyLinkedList:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._head is None

    def add_first(self, element):
        new_node = self._Node(element, self._head)
        self._head = new_node
        self._size += 1

    def add_last(self, element):
        new_node = self._Node(element)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            while current._next:
                current = current._next
            current._next = new_node
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        removed = self._head._element
        self._head = self._head._next
        self._size -= 1
        return removed

    def __iter__(self):
        current = self._head
        while current:
            yield current._element
            current = current._next

    def print_list(self):
        print("Current Linked List")
        if self.is_empty():
            print(" [empty]")
        else:
            current = self._head
            while current:
                end = " -> " if current._next else ""
                print(current._element, end=end)
                current = current._next
            print()


linked_list = SinglyLinkedList()
linked_list.add_first("C")  # List: C
linked_list.add_first("B")  # List: B -> C
linked_list.add_first("A")  # List: A -> B -> C
linked_list.add_last("D")  # List: A -> B -> C -> D

removed = linked_list.remove_first()  # Removes "A"
print(f"Removed: {removed}")

# Print the list
linked_list.print_list()
