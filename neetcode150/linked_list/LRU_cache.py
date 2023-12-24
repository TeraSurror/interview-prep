from typing import Dict, Optional


class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key: int = key
        self.value: int = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity: int):
        # initialize values
        self.capacity: int = capacity
        self.cache: Dict[int, Node] = {}
        self.left: Node = Node(0, 0)
        self.right: Node = Node(0, 0)

        # set up pointers b/w left and right
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from list
    def remove(self, node: Node) -> None:
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

    # insert before right
    def insert(self, node: Node) -> None:
        node.prev = self.right.prev
        node.next = self.right
        if self.right.prev:
            self.right.prev.next = node
            self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # update most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            if self.left.next:
                lru: Node = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
