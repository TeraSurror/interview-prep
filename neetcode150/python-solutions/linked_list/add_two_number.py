from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy: Optional[ListNode] = ListNode()
    curr: Optional[ListNode] = dummy

    sum: int = 0
    carry: int = 0
    while l1 and l2:
        total: int = l1.val + l2.val + carry
        sum = total % 10
        carry = total // 10
        new_node = ListNode(sum)
        curr.next = new_node
        curr = curr.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        total: int = l1.val + carry
        sum = total % 10
        carry = total // 10
        new_node = ListNode(sum)
        curr.next = new_node
        curr = curr.next
        l1 = l1.next

    while l2:
        total: int = l2.val + carry
        sum = total % 10
        carry = total // 10
        new_node = ListNode(sum)
        curr.next = new_node
        curr = curr.next
        l2 = l2.next

    if carry == 1:
        new_node = ListNode(carry)
        curr.next = new_node
        curr = curr.next

    return dummy.next
