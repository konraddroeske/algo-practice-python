from collections import OrderedDict
from typing import Optional


# Solution 1 - Double Linked List

class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        prev_node = None if self.prev is None else self.prev.val
        next_node = None if self.next is None else self.next.val
        return f'val: {self.val}, prev: {prev_node}, next: {next_node}'


class LRULinkedList:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node: Node) -> None:
        """Add after head"""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node) -> None:
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def move_to_head(self, node: Node) -> None:
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self) -> Node:
        res = self.tail.prev
        self.remove_node(res)

        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if node is None:
            return -1

        self.move_to_head(node)

        return node.val

    def put(self, key: int, val: int) -> None:
        node = self.cache.get(key)

        if node:
            node.val = val
            self.move_to_head(node)
        else:
            new_node = Node(key, val)
            self.add_node(new_node)
            self.cache[key] = new_node

            if len(self.cache) > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]


# Solution 2 - Ordered Dict

class LRUCache(OrderedDict):
    def __init__(self, capacity: int) -> None:
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)

        return self[key]

    def put(self, key, value) -> None:
        if key in self:
            self.move_to_end(key)

        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last=False)


lRUCache = LRULinkedList(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)

# lRUCache = LRUCache(1)
# lRUCache.put(2, 1)
# lRUCache.get(2)
# lRUCache.put(3, 2)
# lRUCache.get(2)
# lRUCache.get(3)
