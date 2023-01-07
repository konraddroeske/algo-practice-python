# 1. Every parent node must have at most, 2 children
# 2. Must be a complete tree, except last level
# 3. Min heap, parents key must be smaller than children, or vise versa


class MinHeap:
    def __init__(self, capacity: int):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def get_left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def get_right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def has_parent(self, index) -> bool:
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index: int) -> bool:
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index: int) -> bool:
        return self.get_right_child_index(index) < self.size

    def parent(self, index: int) -> int:
        return self.storage[self.get_parent_index(index)]

    def left_child(self, index: int) -> int:
        return self.storage[self.get_left_child_index(index)]

    def right_child(self, index: int) -> int:
        return self.storage[self.get_right_child_index(index)]

    @property
    def is_full(self) -> bool:
        return self.size == self.capacity

    def swap(self, index_1: int, index_2: int) -> None:
        temp = self.storage[index_1]
        self.storage[index_1] = self.storage[index_2]
        self.storage[index_2] = temp

    def insert(self, data: int) -> None:
        if self.is_full:
            raise Exception("Heap if full.")

        self.storage[self.size] = data
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_up(self, index: int) -> None:
        if self.has_parent(index) \
                and self.parent(index) > self.storage[index]:
            self.swap(self.get_parent_index(index), index)
            self.heapify_up(self.get_parent_index(index))

    def remove_min(self):
        if self.size == 0:
            raise Exception("Empty heap")

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapify_down(0)
        return data

    def heapify_down(self, index: int):
        smallest = index

        if self.has_left_child(index) \
                and self.storage[smallest] > self.left_child(index):
            smallest = self.get_left_child_index(index)

        if self.has_right_child(index) \
                and self.storage[smallest] > self.right_child(index):
            smallest = self.get_right_child_index(index)

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)


test_heap = MinHeap(7)

test_heap.insert(20)
print(test_heap.storage)

test_heap.insert(10)
print(test_heap.storage)

test_heap.insert(5)
print(test_heap.storage)

test_heap.insert(8)
print(test_heap.storage)

test_heap.insert(0)
print(test_heap.storage)

test_heap.remove_min()
print(test_heap.storage)
