from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    def helper(cur_node: Optional[TreeNode]) -> list[int]:
        if cur_node is None:
            return []

        return helper(cur_node.left) + [cur_node.val] + helper(cur_node.right)

    result = helper(root)[k - 1]

    return result


def kth_smallest_iterative(root: Optional[TreeNode], k: int) -> int:
    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        # traverse right
        root = stack.pop()
        k -= 1

        if k == 0:
            return root.val

        root = root.right


input_1 = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
k_1 = 1

print(kth_smallest_iterative(input_1, k_1))

input_2 = TreeNode(
    5,
    left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4)),
    right=TreeNode(6),
)
k_2 = 4

print(kth_smallest_iterative(input_2, k_2))
