from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    if head == None or head.next == None:
        return

    slow: Optional[ListNode] = head
    fast: Optional[ListNode] = head.next
    while slow != None and fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    stack: List[ListNode] = []
    dummy_slow: Optional[ListNode] = slow
    if slow != None:
        slow = slow.next
    while slow != None:
        stack.append(slow)
        slow = slow.next

    if dummy_slow != None:
        dummy_slow.next = None

    curr: Optional[ListNode] = head
    for i in range(len(stack) - 1, -1, -1):
        new_node: Optional[ListNode] = stack[i]
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next
