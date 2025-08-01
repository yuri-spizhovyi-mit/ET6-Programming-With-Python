class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def merge_sorted_lists(l1, l2):
    dummy = ListNode()  # temporary dummy head node
    current = dummy  # will build the result list here

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1  # attach l1 node
            l1 = l1.next
        else:
            current.next = l2  # attach l2 node
            l2 = l2.next
        current = current.next

    # Attach remaining nodes
    current.next = l1 if l1 else l2

    return dummy.next  # skip dummy head


# Build a list from Python list
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


# Print a linked list
def print_list(node):
    while node:
        print(node.val, end=" → " if node.next else "")
        node = node.next
    print()


# Test it
l1 = build_list([1, 3, 5])
l2 = build_list([2, 4, 6])

merged = merge_sorted_lists(l1, l2)
print("Merged list:")
print_list(merged)
