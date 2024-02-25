from typing import Dict, Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    index_dict_old: Dict[Node, int] = {}
    index_dict_new: Dict[int, Node] = {}
    index: int = 0

    if head == None:
        return None

    new_head = Node(head.val)
    dummy = Node(0, new_head)

    curr: Optional[Node] = head

    index_dict_old[head] = index
    index_dict_new[index] = new_head

    index += 1
    curr = curr.next

    while curr != None:
        index_dict_old[curr] = index
        new_head.next = Node(curr.val)
        new_head = new_head.next
        index_dict_new[index] = new_head
        curr = curr.next
        index += 1

    new_head = dummy.next

    curr = head
    curr_new: Optional[Node] = new_head

    while curr != None and curr_new != None:
        if curr.random != None:
            random_index = index_dict_old[curr.random]
            curr_new.random = index_dict_new[random_index]
        curr = curr.next
        curr_new = curr_new.next

    return new_head
