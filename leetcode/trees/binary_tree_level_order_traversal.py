from typing import Optional


class Node:
    def __init__(self, val=None, left=Optional["Node"], right=Optional["Node"]):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[Node]) -> list[list[int]]:
    if root is None:
        return []

    levels = [[root]]
    values: list[list[int]] = [[root.val]]

    while levels:
        cur_level = levels.pop(0)

        next_level = []

        for node in cur_level:
            if node.left is not None:
                next_level.append(node.left)

            if node.right is not None:
                next_level.append(node.right)

        if next_level:
            values.append([node.val for node in next_level])
            levels.append(next_level)

    return values


test_root_1 = Node(
    val=1,
    left=Node(
        val=3,
        left=Node(val=5, left=None, right=None),
        right=Node(val=6, left=None, right=None),
    ),
    right=Node(
        val=2,
        left=Node(val=7, left=Node(val=9, left=None, right=None), right=None),
        right=Node(val=8, left=None, right=None),
    ),
)

print(level_order(test_root_1))
