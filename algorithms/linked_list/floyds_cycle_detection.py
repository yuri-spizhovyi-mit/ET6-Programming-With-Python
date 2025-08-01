class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next  # 1 step
        fast = fast.next.next  # 2 steps
        if slow == fast:
            return True
    return False


# Helper to create a list with a cycle
def create_cyclic_list():
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b  # cycle here

    return a


# Helper to create a list with no cycle
def create_non_cyclic_list():
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    return a


print("Cyclic list:", has_cycle(create_cyclic_list()))  # ✅ True
print("Non-cyclic list:", has_cycle(create_non_cyclic_list()))  # ✅ False
