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


def is_balanced(root: Optional[TreeNode]) -> bool:
    # use dfs
    if root is None:
        return True

    def check_height(cur_root: TreeNode) -> int:
        if cur_root is None:
            return 0

        left_height = check_height(cur_root.left)

        if left_height == -1:
            return -1

        right_height = check_height(cur_root.right)

        if right_height == -1:
            return -1

        height_diff = abs(left_height - right_height)

        if height_diff > 1:
            return -1

        return max(left_height, right_height) + 1

    result = check_height(root)

    if result == -1:
        return False

    return True


input_1 = TreeNode(
    3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
)

input_2 = TreeNode(
    1,
    left=TreeNode(
        2, left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)), right=TreeNode(3)
    ),
    right=TreeNode(2),
)


print(is_balanced(input_1))
print(is_balanced(input_2))
