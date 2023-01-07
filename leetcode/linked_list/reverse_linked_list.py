from typing import Optional

from leetcode.linked_list.list_node import ListNode


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    cur = None

    while head:
        next_node = head.next
        head.next = cur
        cur = head
        head = next_node

    return cur


test_1 = ListNode(
    val=1,
    next=ListNode(
        val=2, next=ListNode(3, next=ListNode(4, next=ListNode(5, next=None)))
    ),
)

reverse_linked_list(test_1)
