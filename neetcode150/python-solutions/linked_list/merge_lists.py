from typing import Optional


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    if list1 == None:
        return list2

    if list2 == None:
        return list1

    head: Optional[Node] = None
    curr: Optional[Node] = None

    while list1 != None and list2 != None:
        new_node: Optional[Node] = None
        if list1.val < list2.val:
            new_node = Node(list1.val)
            list1 = list1.next
        else:
            new_node = Node(list2.val)
            list2 = list2.next

        if curr == None:
            head = curr
            curr = new_node
        else:
            curr.next = new_node
            curr = curr.next

    while curr != None and list1 != None:
        curr.next = Node(list1.val)
        list1 = list1.next
        curr = curr.next

    while curr != None and list2 != None:
        curr.next = Node(list2.val)
        list2 = list2.next
        curr = curr.next

    return head.next if head != None else head
