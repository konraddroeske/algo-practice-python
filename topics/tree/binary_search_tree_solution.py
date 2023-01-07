# all integers to the left are smaller
# all integers to the right are larger
# every node could be a root, living under the same rules
# nodes with no children are "leaf nodes"

# full - all leaf nodes are at the same level
# complete - all levels of the tree are filled except for last leaf, but all nodes to the left
# balanced - no leaf is further from root, than any other leaf

# allows for faster search, insertion, and deletion operations
# worst case it performs like a linked list

from typing import Optional
from random import randint


class Node:
    def __init__(self, value=None):
        self.value: Optional[int] = value
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None
        self.parent: Optional[None] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: int, cur_node: Node) -> None:
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self) -> None:
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node: Node) -> None:
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)

    def height(self) -> int:
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node: Node, cur_height: int) -> int:
        if cur_node is None:
            return cur_height

        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)

        return max(left_height, right_height)

    def find(self, value: int) -> Optional[Node]:
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value: int, cur_node: Node) -> Optional[Node]:
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._find(value, cur_node.right_child)

        return None

    def delete_value(self, value: int) -> None:
        return self.delete_node(self.find(value))

    def delete_node(self, node: Node) -> None:

        def min_value_node(n: Node) -> Node:
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        def num_children(n: Node) -> int:
            count = 0
            if n.left_child is not None:
                count += 1
            if n.right_child is not None:
                count += 1
            return count

        node_parent = node.parent
        node_children = num_children(node)

        if node_children == 0:
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        if node_children == 1:
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            child.parent = node_parent

        if node_children == 2:
            successor = min_value_node(node.right_child)
            node.value = successor.value

            self.delete_node(successor)

    def search(self, value: int) -> bool:
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value: int, cur_node: Node) -> bool:
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._search(value, cur_node.right_child)

        return False


def fill_tree(empty_tree: BinarySearchTree, num_elems=100,
              max_int=1000) -> BinarySearchTree:
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        empty_tree.insert(cur_elem)

    return empty_tree


tree = BinarySearchTree()
# tree = fill_tree(tree)
tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(5)
tree.insert(7)
tree.insert(0)
tree.insert(20)

tree.print_tree()
print("Tree height is:", tree.height())

print(tree.search(20))
print(tree.search(30))

tree.delete_value(3)

tree.print_tree()
