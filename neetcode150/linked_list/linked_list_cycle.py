from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    if head == None or head.next == None:
        return False

    slow: Optional[ListNode] = head
    fast: Optional[ListNode] = head.next

    while slow != None and fast != None:
        if slow == fast:
            return True
        slow = slow.next
        if fast.next != None:
            fast = fast.next.next
        else:
            return False

    return False
