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


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    p_path: list[TreeNode] = []
    q_path: list[TreeNode] = []

    def search(cur_node: TreeNode, target: int, path: list[TreeNode]) -> list[TreeNode]:
        path.append(cur_node)

        if cur_node is None:
            path.pop()
            return path

        if cur_node == target:
            return path

        if target < cur_node.val:
            search(cur_node.left, target, path)

        if target > cur_node.val:
            search(cur_node.right, target, path)

    search(root, p.val, p_path)
    search(root, q.val, q_path)

    for index, p_node in enumerate(p_path):
        if index > len(q_path) - 1:
            return p_path[index - 1]

        if p_node.val != q_path[index].val:
            return p_path[index - 1]

    return p_path[-1]


def lowest_common_ancestor_optimized(
    root: TreeNode, q: TreeNode, p: TreeNode
) -> TreeNode:

    while root:
        # check left
        if q.val < root.val and p.val < root.val:
            root = root.left

        # check right
        elif q.val > root.val and p.val > root.val:
            root = root.right

        # split
        else:
            return root


input_q = TreeNode(val=5)

input_p = TreeNode(
    val=2,
    left=TreeNode(val=0),
    right=TreeNode(4, left=TreeNode(val=3), right=input_q),
)


input_nodes = TreeNode(
    val=6,
    left=input_p,
    right=TreeNode(val=8, left=TreeNode(val=7), right=TreeNode(val=9)),
)


print(lowest_common_ancestor_optimized(input_nodes, input_p, input_q).val)
