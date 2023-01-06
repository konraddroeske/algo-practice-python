from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"


def merge_two_sorted_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    result = ListNode(val=0)
    pointer = result

    while list1 and list2:
        if list1.val < list2.val:
            pointer.next = list1
            list1 = list1.next
        else:
            pointer.next = list2
            list2 = list2.next

        pointer = pointer.next

    if list1 is None:
        pointer.next = list2

    if list2 is None:
        pointer.next = list1

    return result.next


test_1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(4)))
test_2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(4)))

result = merge_two_sorted_lists(test_1, test_2)

print(result)

test_3 = ListNode(val=0, next=None)
test_4 = None

result = merge_two_sorted_lists(test_3, test_4)

print(result)
