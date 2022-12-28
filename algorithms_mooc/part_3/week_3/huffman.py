# 1. a) What is the max length of a codeword in the resulting huffman code?
import sys

sys.setrecursionlimit(10000)

from typing import Optional


with open("./huffman_input.txt") as f:
    full_input = []

    for index, line in enumerate(f):
        if index == 0:
            continue
        else:
            full_input.append(int(line))

# print(full_input)


class Node:
    def __init__(self, weight: int = 0, character: Optional[str] = None):
        self.weight: int = weight
        self.character: Optional[str] = character

        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

        self.code: str = ""

    def __repr__(self) -> str:
        return (
            f"Node(character: {self.character}, weight: {self.weight}, "
            f"code: {self.code})"
        )

    def print_tree(self) -> None:
        stack = [self]
        level = 0

        while stack:
            count = len(stack)
            print(f"Level: {level}")

            while count > 0:
                cur = stack.pop(0)
                print(cur, end=" ")

                if cur.left:
                    stack.append(cur.left)

                if cur.right:
                    stack.append(cur.right)

                count -= 1

            print(" ")
            level += 1


class HuffmanTree:
    # def __init__(self, weights: dict[str, Node]) -> None:
    def __init__(self, weights: list[int]) -> None:
        self.weights = weights
        self.root: Optional[Node] = None

        self.max_codeword: Optional[int] = None
        self.min_codeword: Optional[int] = None

    @staticmethod
    def get_smallest_weights(sigma: dict[str, Node]) -> tuple[Node, Node]:
        sorted_nodes = sorted(sigma.values(), key=lambda x: x.weight)
        return sorted_nodes[0], sorted_nodes[1]

    @staticmethod
    def merge_nodes(sigma: dict[str, Node], a: Node, b: Node) -> dict[str, Node]:
        new_weight = a.weight + b.weight
        new_character = a.character + b.character
        merged_node = Node(new_weight, new_character)
        merged_node.left = a
        merged_node.right = b

        sigma[new_character] = merged_node
        del sigma[a.character]
        del sigma[b.character]

        return sigma

    def create_tree(self) -> None:
        sigma = {
            str(index): Node(weight=weight, character=str(index))
            for index, weight in enumerate(self.weights)
        }
        # sigma = {}

        # self.root = self._create_tree(self.weights)
        self.root = self._create_tree(sigma)

    def _create_tree(self, sigma: dict[str, Node]) -> Node:
        if len(sigma) == 2:
            nodes = [node for node in sigma.values()]
            left_node = nodes[0]
            right_node = nodes[1]
            parent_characters = left_node.character + right_node.character
            parent_weight = left_node.weight + right_node.weight

            parent_node = Node(weight=parent_weight, character=parent_characters)
            parent_node.left = nodes[0]
            parent_node.right = nodes[1]

            return parent_node

        a, b = self.get_smallest_weights(sigma)
        sigma_prime = self.merge_nodes(sigma, a, b)

        parent_node = self._create_tree(sigma_prime)

        # Assign Codes
        self.assign_codes(parent_node)

        return parent_node

    def set_max_codeword(self, cur_node: Node) -> None:
        if self.max_codeword is None:
            self.max_codeword = len(cur_node.code)
        else:
            self.max_codeword = max(self.max_codeword, len(cur_node.code))

    def set_min_codeword(self, cur_node: Node) -> None:
        if len(cur_node.character) == 1:
            if self.min_codeword is None:
                self.min_codeword = len(cur_node.code)
            else:
                self.min_codeword = min(self.min_codeword, len(cur_node.code))

    def assign_codes(self, root: Node) -> None:
        stack = [root]
        level = 0

        while stack:
            count = len(stack)

            while count > 0:
                cur = stack.pop(0)
                self.set_max_codeword(cur)
                self.set_min_codeword(cur)

                if cur.left:
                    cur.left.code = cur.code + "1"
                    stack.append(cur.left)

                if cur.right:
                    cur.right.code = cur.code + "0"
                    stack.append(cur.right)

                count -= 1

            level += 1


test_input = [3, 2, 6, 8, 2, 6]
# test_input = {
#     "A": Node(3, "A"),
#     "B": Node(2, "B"),
#     "C": Node(6, "C"),
#     "D": Node(8, "D"),
#     "E": Node(2, "E"),
#     "F": Node(6, "F"),
# }


test_tree = HuffmanTree(full_input)
test_tree.create_tree()
print(f"Max code: {test_tree.max_codeword}")
print(f"Min code: {test_tree.min_codeword}")
# test_tree.root.print_tree()


# Results 19, 9
