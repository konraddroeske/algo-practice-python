from math import floor
from typing import Optional


class MinHeap:
    def __init__(self) -> None:
        self.heap: list[int] = []

    def __repr__(self) -> str:
        return f"{self.heap}"

    @property
    def min(self) -> Optional[int]:
        if len(self.heap) > 0:
            return self.heap[0]

        return None

    @staticmethod
    def get_parent_pos(cur_pos: int) -> int:
        if cur_pos == 1:
            return 1

        if cur_pos % 2 == 0:
            return int(cur_pos / 2)

        return floor(cur_pos / 2)

    def insert(self, new_key: int) -> None:
        self.heap.append(new_key)

        if len(self.heap) == 1:
            return

        cur_pos = len(self.heap)
        parent_pos = self.get_parent_pos(cur_pos)

        while self.heap[cur_pos - 1] < self.heap[parent_pos - 1]:
            self.swap(cur_pos, parent_pos)

            cur_pos = parent_pos
            parent_pos = self.get_parent_pos(cur_pos)

    def get_left_child(self, cur_pos: int) -> tuple[int, Optional[int]]:
        pos = cur_pos * 2

        if pos <= len(self.heap):
            key = self.heap[pos - 1]
        else:
            key = None

        return pos, key

    def get_right_child(self, cur_pos: int) -> tuple[int, Optional[int]]:
        pos = (cur_pos * 2) + 1

        if pos <= len(self.heap):
            key = self.heap[pos - 1]
        else:
            key = None

        return pos, key

    def swap(self, pos_1: int, pos_2: int) -> None:
        self.heap[pos_1 - 1], self.heap[pos_2 - 1] = (
            self.heap[pos_2 - 1],
            self.heap[pos_1 - 1],
        )

    def get_min_child(self, cur_pos: int) -> Optional[tuple[int, int]]:
        left_pos, left_key = self.get_left_child(cur_pos)
        right_pos, right_key = self.get_right_child(cur_pos)

        if right_key and not left_key:
            return right_pos, right_key

        if left_key and not right_key:
            return left_pos, left_key

        if right_key and left_key:
            if right_key < left_key:
                return right_pos, right_key

            if left_key < right_key:
                return left_pos, left_key

        # print(f"Cannot get minimum child from: {cur_pos}")
        return None

    def extract_min(self) -> Optional[int]:
        if len(self.heap) == 0:
            print("Heap is empty, cannot extract min.")
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        cur_pos = 1
        root = self.heap[cur_pos - 1]

        last_leaf = self.heap.pop()
        self.heap[cur_pos - 1] = last_leaf

        min_child = self.get_min_child(cur_pos)

        if not min_child:
            return root

        min_pos, min_key = min_child

        while min_child and min_key < last_leaf:
            self.swap(cur_pos, min_pos)
            cur_pos = min_pos

            min_child = self.get_min_child(cur_pos)

            if not min_child:
                break

            min_pos, min_key = min_child

        return root


class MaxHeap:
    def __init__(self) -> None:
        self.heap: list[int] = []

    def __repr__(self) -> str:
        return f"{self.heap}"

    @property
    def max(self) -> Optional[int]:
        if len(self.heap) > 0:
            return self.heap[0]

        return None

    @staticmethod
    def get_parent_pos(cur_pos: int) -> int:
        if cur_pos == 1:
            return 1

        if cur_pos % 2 == 0:
            return int(cur_pos / 2)

        return floor(cur_pos / 2)

    def insert(self, new_key: int) -> None:
        self.heap.append(new_key)

        if len(self.heap) == 1:
            return

        cur_pos = len(self.heap)
        parent_pos = self.get_parent_pos(cur_pos)

        while self.heap[cur_pos - 1] > self.heap[parent_pos - 1]:
            self.swap(cur_pos, parent_pos)

            cur_pos = parent_pos
            parent_pos = self.get_parent_pos(cur_pos)

    def get_left_child(self, cur_pos: int) -> tuple[int, Optional[int]]:
        pos = cur_pos * 2

        if pos <= len(self.heap):
            key = self.heap[pos - 1]
        else:
            key = None

        return pos, key

    def get_right_child(self, cur_pos: int) -> tuple[int, Optional[int]]:
        pos = (cur_pos * 2) + 1

        if pos <= len(self.heap):
            key = self.heap[pos - 1]
        else:
            key = None

        return pos, key

    def swap(self, pos_1: int, pos_2: int) -> None:
        self.heap[pos_1 - 1], self.heap[pos_2 - 1] = (
            self.heap[pos_2 - 1],
            self.heap[pos_1 - 1],
        )

    def get_max_child(self, cur_pos: int) -> Optional[tuple[int, int]]:
        left_pos, left_key = self.get_left_child(cur_pos)
        right_pos, right_key = self.get_right_child(cur_pos)

        if right_key and not left_key:
            return right_pos, right_key

        if left_key and not right_key:
            return left_pos, left_key

        if right_key and left_key:
            if left_key > right_key:
                return left_pos, left_key

            if right_key > left_key:
                return right_pos, right_key

        # print(f"Cannot get minimum child from: {cur_pos}")
        return None

    def extract_max(self) -> Optional[int]:
        if len(self.heap) == 0:
            print("Heap is empty, cannot extract min.")
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        cur_pos = 1
        root = self.heap[cur_pos - 1]

        last_leaf = self.heap.pop()
        self.heap[cur_pos - 1] = last_leaf

        max_child = self.get_max_child(cur_pos)

        if not max_child:
            return root

        max_pos, max_key = max_child

        while max_child and max_key > last_leaf:
            self.swap(cur_pos, max_pos)
            cur_pos = max_pos

            max_child = self.get_max_child(cur_pos)

            if not max_child:
                break

            max_pos, max_key = max_child

        return root


input = [20, 3, 5, 1, 10, 12]

h_low = MaxHeap()
h_high = MinHeap()

medians = []


def handle_insert(new_val: int) -> None:
    if h_low.max and new_val < h_low.max:
        h_low.insert(new_val)
        return

    if h_high.min and new_val > h_high.min:
        h_high.insert(new_val)
        return

    h_low.insert(new_val)
    return


def handle_imbalance() -> None:
    if len(h_low.heap) - len(h_high.heap) > 1:
        extracted = h_low.extract_max()
        h_high.insert(extracted)

    if len(h_high.heap) - len(h_low.heap) > 1:
        extracted = h_high.extract_min()
        h_low.insert(extracted)


# for i, val in enumerate(input, 1):
#     handle_insert(val)
#     handle_imbalance()
#
#     if i % 2 == 0:
#         if h_low.max:
#             medians.append(h_low.max)
#         else:
#             medians.append(h_high.min)
#
#     else:
#         if len(h_low.heap) > len(h_high.heap):
#             medians.append(h_low.max)
#         else:
#             medians.append(h_high.min)
#
#     print("h low", h_low)
#     print("h high", h_high)
#     print("medians", medians)

with open("median_maintenance_input.txt") as f:
    for i, line in enumerate(f, 1):
        val = int(line)

        handle_insert(val)
        handle_imbalance()

        if i % 2 == 0:
            if h_low.max:
                medians.append(h_low.max)
            else:
                medians.append(h_high.min)

        else:
            if len(h_low.heap) > len(h_high.heap):
                medians.append(h_low.max)
            else:
                medians.append(h_high.min)

print(len(medians))
print(sum(medians) % 10000)
