class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def merge_sorted_lists_recursive(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1

    if l1.val < l2.val:
        l1.next = merge_sorted_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_lists_recursive(l1, l2.next)
        return l2


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def print_list(node):
    while node:
        print(node.val, end=" → " if node.next else "")
        node = node.next
    print()


# Test it
l1 = build_list([1, 3, 5])
l2 = build_list([2, 4, 6])

merged = merge_sorted_lists_recursive(l1, l2)
print("Merged list (recursive):")
print_list(merged)
