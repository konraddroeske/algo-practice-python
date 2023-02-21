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
        return f"TreeNode(val={self.val}, left={self.left}, right=" f"{self.right})"


def sorted_array_to_bst(nums: list[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    mid = len(nums) // 2
    mid_node = TreeNode(nums[mid])

    mid_node.right = sorted_array_to_bst(nums[mid + 1 :])
    mid_node.left = sorted_array_to_bst(nums[:mid])

    return mid_node


def sorted_array_to_bst_with_pivots(nums: list[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    def helper(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        mid = (left + right) // 2

        if mid % 2 == 0:
            mid += 1

        mid_node = TreeNode(nums[mid])
        mid_node.left = helper(left, mid - 1)
        mid_node.right = helper(mid + 1, right)

        return mid_node

    return helper(0, len(nums) - 1)


input_1 = [-10, -3, 0, 5, 9]
print(sorted_array_to_bst(input_1))

input_2 = [1, 3]
print(sorted_array_to_bst(input_2))
