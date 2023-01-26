from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val}, {self.next})"


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head is None or head.next is None:
        return None

    dummy = ListNode(0, head)

    fast = dummy
    slow = dummy

    for index in range(n + 1):
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


input_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(remove_nth_from_end(input_1, 2))

input_1 = ListNode(1, None)
print(remove_nth_from_end(input_1, 1))

input_1 = ListNode(1, ListNode(2, None))
print(remove_nth_from_end(input_1, 1))

input_1 = ListNode(1, ListNode(2, None))
print(remove_nth_from_end(input_1, 2))
