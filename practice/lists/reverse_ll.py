class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    while head:
        next_node = head.next  # Step 1: store next node
        head.next = prev  # Step 2: reverse the pointer
        prev = head  # Step 3: move prev forward
        head = next_node  # Step 4: move head forward
    return prev


# Helper to build linked list from Python list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper to print linked list
def print_list(head):
    while head:
        print(head.val, end=" → ")
        head = head.next
    print("None")


# Test the reverse function
head = build_linked_list([1, 2, 3, 4, 5])
print("Original list:")
print_list(head)

reversed_head = reverse_list(head)
print("Reversed list:")
print_list(reversed_head)
