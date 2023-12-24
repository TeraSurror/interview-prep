from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            l1: Optional[ListNode] = lists[i]
            l2: Optional[ListNode] = lists[i + 1] if (i + 1) < len(lists) else None
            merged_list: Optional[ListNode] = merge_2_sorted_lists(l1, l2)
            merged_lists.append(merged_list)

        lists = merged_lists

    return lists[0]


def merge_2_sorted_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    if not l1:
        return l2

    if not l2:
        return l1

    curr = ListNode()
    dummy = curr

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = ListNode(l1.val)
            l1 = l1.next
        else:
            curr.next = ListNode(l2.val)
            l2 = l2.next
        curr = curr.next

    while l1:
        curr.next = ListNode(l1.val)
        l1 = l1.next
        curr = curr.next

    while l2:
        curr.next = ListNode(l2.val)
        l2 = l2.next
        curr = curr.next

    return dummy.next
