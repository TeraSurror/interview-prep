from typing import Optional


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[Node]) -> Optional[Node]:
    prev: Optional[Node] = None
    curr: Optional[Node] = head

    while curr != None:
        next: Optional[Node] = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head = prev

    return head
