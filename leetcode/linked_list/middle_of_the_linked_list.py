from math import ceil
from typing import Optional

from leetcode.linked_list.list_node import ListNode


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    counter = 0
    nodes = {}

    while head:
        counter += 1
        nodes[counter] = head
        head = head.next

    return nodes[ceil((counter + 1) / 2)]

def middle_node_pointers(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


test_1 = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None))),
    ),
)

test_2 = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(
            val=3,
            next=ListNode(val=4, next=ListNode(val=5, next=ListNode(val=6, next=None))),
        ),
    ),
)

test_3 = ListNode(val=1, next=ListNode(val=2, next=None))

print(middle_node_pointers(test_1))
print(middle_node_pointers(test_2))
print(middle_node_pointers(test_3))
