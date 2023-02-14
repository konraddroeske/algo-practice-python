from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node(val={self.val}, left={self.left}, right={self.right})"


def invert_tree(root: TreeNode) -> TreeNode:
    if not root:
        return root

    stack = deque([root])

    while stack:
        cur_node = stack.popleft()
        cur_node.left, cur_node.right = cur_node.right, cur_node.left

        if cur_node.left:
            stack.append(cur_node.left)

        if cur_node.right:
            stack.append(cur_node.right)

    return root


def invert_tree_recursive(root: TreeNode) -> TreeNode:
    if not root:
        return root

    right = invert_tree_recursive(root.right)
    left = invert_tree_recursive(root.left)

    root.right = left
    root.left = right

    return root


root_1 = TreeNode(2, left=TreeNode(1), right=TreeNode(3))


inverted = invert_tree(root_1)

print(inverted)
