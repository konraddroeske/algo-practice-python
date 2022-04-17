from typing import Optional


class ListNode(object):
    def __init__(self, val: Optional[int] = 0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self):
        return f'Val: {self.val}'


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    if len(lists) == 0:
        return None

    nodes = []

    for linked_list in lists:
        while linked_list is not None:
            nodes.append(ListNode(linked_list.val))
            linked_list = linked_list.next

    if not nodes:
        return None

    sorted_nodes = sorted(nodes, key=lambda x: x.val)

    if len(sorted_nodes) == 1:
        return sorted_nodes[0]

    if len(sorted_nodes) >= 2:
        for i in range(1, len(sorted_nodes)):
            sorted_nodes[i - 1].next = sorted_nodes[i]

    return sorted_nodes[0]


list_1 = ListNode(1, ListNode(4, ListNode(5)))
list_2 = ListNode(1, ListNode(3, ListNode(4)))
list_3 = ListNode(2, ListNode(3))

result = merge_k_lists([list_1, list_2, list_3])
result_2 = merge_k_lists([None])

# whether we fill to the top, throw it out, or transfer.
# so that we can have instructions on how to achieve the goal.
