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


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]) -> None:
        self.stack = []
        self.traverse_left(root)

    def traverse_left(self, root: TreeNode) -> None:
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        root = self.stack.pop()

        if root.right:
            self.traverse_left(root.right)

        return root.val

    def has_next(self) -> bool:
        return bool(self.stack)


input_1 = TreeNode(
    7, left=TreeNode(3), right=TreeNode(15, left=TreeNode(9), right=TreeNode(20))
)

iterator = BSTIterator(input_1)

print(iterator.next())
print(iterator.next())
print(iterator.has_next())
print(iterator.next())
print(iterator.has_next())
print(iterator.next())
print(iterator.has_next())
print(iterator.next())
print(iterator.has_next())
