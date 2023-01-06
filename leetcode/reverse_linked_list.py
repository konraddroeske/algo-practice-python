from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"


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
