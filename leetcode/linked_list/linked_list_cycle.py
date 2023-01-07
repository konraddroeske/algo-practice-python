from typing import Optional

from leetcode.linked_list.list_node import ListNode


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return None

    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast and fast == slow:
            while head != slow:
                head = head.next
                slow = slow.next

            return head

    return None


# test_case = [-1, -7, 7, -4, 19, 6, -9, -5, -2, -5]
# 6

node_1 = ListNode(val=-1)
node_2 = ListNode(val=-7)
node_3 = ListNode(val=7)
node_4 = ListNode(val=-4)
node_5 = ListNode(val=19)
node_6 = ListNode(val=6)
node_7 = ListNode(val=-9)
node_8 = ListNode(val=-5)
node_9 = ListNode(val=-2)
node_10 = ListNode(val=-5)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6
node_6.next = node_7
node_7.next = node_8
node_8.next = node_9
node_9.next = node_10
node_10.next = node_10

print(detect_cycle(node_1))
