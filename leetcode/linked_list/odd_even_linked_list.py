from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None) -> None:
        self.val = val
        self.next = next


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    # traverse to end
    fast = head
    slow = head
    length = 0

    while fast.next:
        fast = fast.next
        length += 1

    if length < 2:
        return head

    for index in range(length):
        if index % 2 == 0:
            cur_node = slow.next
            next_node = cur_node.next

            cur_node.next = None
            fast.next = cur_node
            fast = fast.next

            slow.next = next_node
        else:
            slow = slow.next

    return head

input_1 = ListNode(1, ListNode(2))
# input_2 = ListNode(
#     1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))
# )

result = odd_even_list(input_1)

while result:
    print("result", result.val)
    result = result.next
