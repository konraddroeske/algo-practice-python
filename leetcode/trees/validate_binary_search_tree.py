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


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    nodes_in_order: list[TreeNode] = []

    def in_order_traversal(cur_node: Optional[TreeNode], nodes: list[TreeNode]) -> None:
        if cur_node is not None:
            in_order_traversal(cur_node.left, nodes)
            nodes.append(cur_node)
            in_order_traversal(cur_node.right, nodes)

    in_order_traversal(root, nodes_in_order)

    for index, node in enumerate(nodes_in_order):
        if index == 0:
            continue

        if node.val <= nodes_in_order[index - 1].val:
            return False

    return True


def is_valid_bst_optimized(root: Optional[TreeNode]) -> bool:
    prev = [None]
    result = [True]

    def in_order_traversal(
        cur_node: Optional[TreeNode],
        prev: list[Optional[TreeNode]],
        is_valid: list[bool],
    ) -> None:

        if cur_node is not None:
            in_order_traversal(cur_node.left, prev, is_valid)

            if prev[0] is not None and prev[0].val >= cur_node.val:
                is_valid[0] = False

            prev[0] = cur_node
            in_order_traversal(cur_node.right, prev, is_valid)

    in_order_traversal(root, prev, result)

    return result[0]


input_nodes = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))
# input_nodes = TreeNode(val=1, left=TreeNode(val=1))


print(is_valid_bst_optimized(input_nodes))
