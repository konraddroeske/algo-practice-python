from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None) -> None:
        self.val = val
        self.next = next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    nodes = []

    while head:
        nodes.append(head)
        head = head.next

    nodes.sort(key=lambda x: x.val)

    for index, node in enumerate(nodes):
        if index + 1 < len(nodes):
            node.next = nodes[index + 1]
        else:
            node.next = None

    return nodes[0]


def sort_list_optimized(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    def get_middle(cur_head: ListNode) -> ListNode:
        slow = None

        while cur_head and cur_head.next:
            slow = head if slow is None else slow.next
            cur_head = cur_head.next.next

        middle = slow.next
        slow.next = None

        return middle

    def merge(cur_left: ListNode, cur_right: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while cur_left and cur_right:
            if cur_left.val < cur_right.val:
                tail.next = cur_left
                tail = tail.next
                cur_left = cur_left.next
            else:
                tail.next = cur_right
                tail = tail.next
                cur_right = cur_right.next

        tail.next = cur_left if cur_left else cur_right

        return dummy.next

    mid = get_middle(head)
    left = sort_list_optimized(head)
    right = sort_list_optimized(mid)

    return merge(left, right)


input_1 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

result_1 = sort_list_optimized(input_1)

while result_1:
    print(result_1.val)
    result_1 = result_1.next
