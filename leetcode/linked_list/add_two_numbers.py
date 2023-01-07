from typing import Optional

from leetcode.linked_list.list_node import ListNode


# 1 - Brute Force
# Iterate through both linked lists, add number to front of string, convert to int,
# add, then return as linked lists

# Time Complexity = n


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    num_1 = ""
    num_2 = ""

    while l1 is not None:
        num_1 = str(l1.val) + num_1
        l1 = l1.next

    while l2 is not None:
        num_2 = str(l2.val) + num_2
        l2 = l2.next

    sum = str(int(num_1) + int(num_2))

    result = []

    for i, val in enumerate(sum):
        new_node = ListNode(val)
        result.append(new_node)

        if i - 1 >= 0:
            new_node.next = result[i - 1]

    return result[-1]


# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

input_l1_vals = [9, 9, 9, 9, 9, 9, 9]
input_l2_vals = [9, 9, 9, 9]

input_l1_arr = []
input_l2_arr = []

for val in input_l1_vals:
    new_node = ListNode(val)

    if len(input_l1_arr):
        prev_node = input_l1_arr[-1]
        prev_node.next = new_node

    input_l1_arr.append(new_node)

for val in input_l2_vals:
    new_node = ListNode(val)

    if len(input_l2_arr):
        prev_node = input_l2_arr[-1]
        prev_node.next = new_node

    input_l2_arr.append(new_node)

input_l1 = input_l1_arr[0]
input_l2 = input_l2_arr[0]


# 2 - Use Math and use the Carry


def add_two_numbers_carry(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode(0)
    curr = dummy_head

    carry = 0

    while l1 or l2 or carry:
        l1_val = 0 if l1 is None else l1.val
        l2_val = 0 if l2 is None else l2.val

        new_val = l1_val + l2_val + carry

        if new_val >= 10:
            carry = new_val // 10
            new_val = new_val % 10
        else:
            carry = 0

        new_node = ListNode(new_val)

        curr.next = new_node
        curr = new_node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy_head.next


result = add_two_numbers_carry(input_l1, input_l2)

# for node in result:
while result:
    print("val", result.val)
    result = result.next
