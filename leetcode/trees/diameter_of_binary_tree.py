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


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    max_diameter = 0

    def check_diameter(cur_root: TreeNode) -> int:
        if cur_root is None:
            return 0

        nonlocal max_diameter

        left_height = check_diameter(cur_root.left)
        right_height = check_diameter(cur_root.right)

        max_diameter = max(max_diameter, left_height + right_height)

        return max(left_height, right_height) + 1

    check_diameter(root)

    return max_diameter


input_1 = TreeNode(
    1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3)
)

input_2 = TreeNode(1, left=TreeNode(2))

print(diameter_of_binary_tree(input_1))
print(diameter_of_binary_tree(input_2))
