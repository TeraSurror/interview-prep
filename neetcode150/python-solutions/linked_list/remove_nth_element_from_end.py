from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> None:
    dummy: Optional[ListNode] = ListNode(0, head)

    start: Optional[ListNode] = dummy
    end: Optional[ListNode] = head

    while n > 0 and end != None:
        end = end.next
        n -= 1

    while start and end:
        start = start.next
        end = end.next

    if start != None and start.next != None:
        start.next = start.next.next

    return dummy.next
