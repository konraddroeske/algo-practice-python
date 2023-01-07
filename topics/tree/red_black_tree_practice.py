# Source: https://www.youtube.com/watch?v=p8TSYkDz0eI

# Rules

# 1. Every node is either red or black. (Use boolean to note red or black)
# 2. Root is always black
# 3. New insertions are always red
# 4. Every path from root to leaf has the same number of BLACK nodes
# 5. No path can have two consecutive RED nodes
# 6. Nulls are black

# Rebalance:
# - If we have a BLACK aunt we rotate
# - If we have a RED aunt we color flip

# After Rotation:
# Parent: Black
# Children: Red

# After Colorflip:
# Parent: Red
# Children: Black

class Node:
    def __init__(self, value=None) -> None:
        self.is_black = False
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.is_left_child = False


class RedBlackTree:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def add(self, value: int) -> None:
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            self.root.is_black = True
            self.size += 1
            return

        self._add(self.root, new_node)
        self.size += 1

    def _add(self, cur_node: Node, new_node: Node) -> None:
        if new_node.value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = new_node
                new_node.parent = cur_node
                new_node.is_left_child = True
            else:
                self._add(cur_node.left_child, new_node)

        elif new_node.value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = new_node
                new_node.parent = cur_node
                new_node.is_left_child = False
            else:
                self._add(cur_node.right_child, new_node)

        else:
            print('Value already in tree!')
