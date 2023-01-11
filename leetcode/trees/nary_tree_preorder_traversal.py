class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root: "Node") -> list[int]:
    if root is None:
        return []

    def dfs(cur_node: "Node", vals: list[int]) -> list[int]:
        if cur_node.children is None:
            return vals + [cur_node.val]

        for child in cur_node.children:
            vals += [child.val]
            dfs(child, vals)

    result = [root.val]
    dfs(root, result)

    return result


test_root_1 = Node(
    val=1,
    children=[
        Node(
            val=3,
            children=[
                Node(val=5, children=None),
                Node(val=6, children=None),
            ],
        ),
        Node(val=2, children=None),
        Node(val=4, children=None),
    ],
)

print(preorder(test_root_1))
