from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"


def sub_array_sum(nums: list[int], k: int) -> int:
    count = 0
    curr_sum = 0
    h = defaultdict(int)

    for num in nums:
        curr_sum += num

        if curr_sum == k:
            count += 1

        count += h[curr_sum - k]

        h[curr_sum] += 1

    return count


# input_1 = [3, 4, 1, 6, 1, 6, -3]
# target_1 = 7
#
# print(sub_array_sum(input_1, target_1))


def path_sum(root: Optional[TreeNode], target: int) -> int:
    count = 0
    prefix_sum = defaultdict(int)

    def traverse(cur_node: Optional[TreeNode], cur_sum: int) -> None:
        if cur_node is None:
            return

        nonlocal count

        cur_sum += cur_node.val

        if cur_sum == target:
            count += 1

        count += prefix_sum[cur_sum - target]

        prefix_sum[cur_sum] += 1

        # print(cur_node.val)

        traverse(cur_node.left, cur_sum)
        traverse(cur_node.right, cur_sum)

        print(cur_node.val)
        prefix_sum[cur_sum] -= 1

    traverse(root, 0)

    return count


input_1 = TreeNode(
    10,
    left=TreeNode(
        5,
        left=TreeNode(3, left=TreeNode(3), right=TreeNode(-2)),
        right=TreeNode(2, right=TreeNode(1)),
    ),
    right=TreeNode(-3, right=TreeNode(11)),
)
target_1 = 8


path_sum(input_1, target_1)
