from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None) -> None:
        self.val = val
        self.next = next


def is_palindrome(head: Optional[ListNode]) -> bool:
    arr = []

    while head:
        arr.append(head.val)
        head = head.next

    return arr == arr[::-1]


def is_palindrome_mem_optimized(head: Optional[ListNode]) -> bool:
    if not head.next:
        return True

    fast = head
    slow = head

    reversed_list = None
    length = 0

    while fast:
        try:
            fast = fast.next.next
            length += 2
        except AttributeError:
            length += 1
            break

        next_node = slow.next
        slow.next = reversed_list
        reversed_list = slow
        slow = next_node

    print("length", length)
    if length % 2 != 0:
        slow = slow.next

    while slow and reversed_list:
        if slow.val != reversed_list.val:
            return False

        slow = slow.next
        reversed_list = reversed_list.next

    return True


input_1 = ListNode(
    val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1)))
)

input_2 = ListNode(
    val=1,
    next=ListNode(val=2),
)

input_3 = ListNode(val=1, next=ListNode(val=0, next=ListNode(val=1)))

print(is_palindrome_mem_optimized(input_1))
print("")
print(is_palindrome_mem_optimized(input_2))
print("")
print(is_palindrome_mem_optimized(input_3))
