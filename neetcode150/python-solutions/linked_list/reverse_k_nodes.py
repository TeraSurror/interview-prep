from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next == None:
            return head

        dummy: Optional[ListNode] = ListNode(0, head)
        group_prev: Optional[ListNode] = dummy

        while True:
            kth: Optional[ListNode] = self.get_kth_node(group_prev, k)
            if not kth:
                break
            group_next: Optional[ListNode] = kth.next

            prev: Optional[ListNode] = group_next
            curr: Optional[ListNode] = group_prev.next
            while curr != group_next:
                nxt: Optional[ListNode] = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tmp: Optional[ListNode] = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def get_kth_node(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
