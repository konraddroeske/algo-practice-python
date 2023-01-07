# Properties
# All nodes to the left have a smaller value
# All nodes to the right have a larget value
# Each node is also a binary search tree

# Create node class
# Value (int), Left Child (Node), Right Child (Node), Parent (Optional Node)
from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


# Create tree class
class BinarySearchTree:
    # init with root node
    def __init__(self):
        self.root: Optional[Node] = None

    # Methods - Insert (None), Get Height (int), Find Node (Optional Node),
    # Delete Node (None), Exists (bool)

    # Insert
    # If root is none, set root to node
    # else, call _insert with value and root
    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    # _Insert
    # if value is less than cur node value,
    # if cur node's left child is none, set equal to node w/ value,
    # set new node's parent to cur node
    # else, call insert again with left child

    # if value is greater than cur node value,
    # if cur node's right child is none, set equal to node w/ value,
    # set new node's parent to cur node
    # else, call insert again with right child
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
            raise ValueError("Value already in Tree.")

    # Height
    # if root is none, return 0
    # else, return _height with root and cur height of 0
    def height(self) -> int:
        if self.root is None:
            return 0
        else:
            return self._height(self.root, 0)

    # _Height
    # initial condition: if cur node is None, return cur_height
    # left height = _height with cur node's left child and height + 1
    # right height = _height with cur node's right child and height + 1
    # return max of left height and right height
    def _height(self, cur_node: Node, cur_height: int) -> int:
        if cur_node is None:
            return cur_height

        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)

        return max(left_height, right_height)

    # Find
    # if roo is none return none
    # else return _find with value and root
    def find(self, value: int) -> Optional[Node]:
        if self.root is None:
            return None
        else:
            return self._find(value, self.root)

    # _Find
    # if value equals cur node value, return cur node
    # else if value < cur node value, and left node is not none,
    # return _find with value and left child
    # else if value > cur node value, and right node is not none,
    # return _find with value and right child

    # return None
    def _find(self, value: int, cur_node: Node) -> Optional[Node]:
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._find(value, cur_node.right_child)

        return None

    # Exists
    # if root node is None, return False
    # else return _Exists with value and root
    def exists(self, value: int) -> bool:
        if self.root is None:
            return False
        else:
            return self._exists(value, self.root)

    # _Exists
    # if value equal cur node value, return True
    # else if value < cur node value and left child is not None,
    # return _Exists with value and left child
    # else if value > cur node value and right child is not None
    # return _Exists with value and right child

    # return False
    def _exists(self, value: int, cur_node: Node) -> bool:
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._exists(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._exists(value, cur_node.right_child)

        return False

    # Delete

    # Delete Value
    # Use Find Value to get node, then return Delete Node w/ Node
    def delete(self, value: int) -> None:
        self._delete(self.find(value))

    # Delete Node
    # Get parent node
    # Get number of child nodes
    def _delete(self, cur_node: Node) -> None:
        def number_of_children(node: Node) -> int:
            count = 0
            if node.left_child is not None:
                count += 1
            if node.right_child is not None:
                count += 1

            return count

        parent = cur_node.parent
        children = number_of_children(cur_node)

        # if node children is 0:
        # if parent left child == node, set parent left child = None
        # else set parent right child = None
        if children == 0:
            if parent.left_child == cur_node:
                parent.left_child = None
            else:
                parent.right_child = None



# if node children is 1:
# if node left child is not None, set child to node left child
# else set child to node right child
# if parent left child == node, set parent left child = child
# else set parent right child = child

# if node children is 2:
# find successor node (min node value of left nodes starting from right child)
# set current node to value of successor
# recursively call delete node on successor
