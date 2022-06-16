# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x: int, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node(val: {self.val}, left: {self.left.val if self.left else None}, ' \
               f'right: {self.right.val if self.right else None})'


class Solution:
    def shortest_path(
            self,
            val: int,
            parent: dict[int, int],
            path: list[int],
            other_path: list[int],
    ) -> Optional[int]:
        path.append(val)

        if val in other_path:
            return val

        if val == parent[val]:
            return None

        new_val = parent[val]
        return self.shortest_path(new_val, parent, path, other_path)

    def bfs(self, root: TreeNode, target: TreeNode) -> dict[int, TreeNode]:
        stack = [root]
        parents = dict()
        parents[root.val] = root

        while stack:
            cur = stack.pop()

            if cur.val == target.val:
                break

            if cur.left:
                parents[cur.left.val] = cur
                stack.append(cur.left)

            if cur.right:
                parents[cur.right.val] = cur
                stack.append(cur.right)

        return parents

    def dfs(self, root: TreeNode, target: TreeNode, path: list[TreeNode]) \
            -> bool:
        path.append(root)

        if root.val == target.val:
            return True

        if root.left and self.dfs(root.left, target, path):
            return True

        if root.right and self.dfs(root.right, target, path):
            return True

        return False

    def lowestCommonAncestor(
            self,
            root: TreeNode,
            p: TreeNode,
            q: TreeNode) -> TreeNode:

        p_parents = self.bfs(root, p)
        q_parents = self.bfs(root, q)

        ancestors = set()

        ancestors.add(q)
        ancestors.add(p)

        p_val = p.val

        while p_val != root.val:
            parent_node = p_parents[p_val]

            if parent_node in ancestors:
                return parent_node

            ancestors.add(parent_node)
            p_val = parent_node.val

        q_val = q.val

        while q_val != root.val:
            parent_node = q_parents[q_val]

            if parent_node in ancestors:
                return parent_node

            ancestors.add(parent_node)
            q_val = parent_node.val


root_1 = TreeNode(
    x=3,
    left=TreeNode(
        x=5,
        left=TreeNode(
            x=6,
        ),
        right=TreeNode(
            x=2,
            left=TreeNode(
                x=7
            ),
            right=TreeNode(
                x=4
            )
        )
    ),
    right=TreeNode(
        x=1,
        left=TreeNode(
            x=0
        ),
        right=TreeNode(
            x=8
        )
    )
)

p_1 = TreeNode(
    x=7,
)

q_1 = TreeNode(
    x=8
)

solution = Solution()

solution.lowestCommonAncestor(root_1, p_1, q_1)
