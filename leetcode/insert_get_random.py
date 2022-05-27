from random import randint


class RandomizedSet:
    def __init__(self) -> None:
        self.pos = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            index = self.pos[val]
            last = self.nums[-1]

            # swap positions between val and last item of list
            self.nums[index] = last

            # replace the position of last
            self.pos[last] = index

            self.nums.pop()
            self.pos.pop(val, 0)

            return True

        return False

    def getRandom(self) -> int:
        index = randint(0, len(self.nums) - 1)
        return self.nums[index]


obj = RandomizedSet()
obj.insert(1)
obj.remove(2)
obj.insert(2)
obj.getRandom()
obj.remove(1)
obj.insert(2)
obj.getRandom()
