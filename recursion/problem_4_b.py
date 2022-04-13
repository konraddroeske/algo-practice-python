# and if this is very easy for you, what if we have arbitrary number of buckets,
# lets say N=5 buckets, which can be filled with A, B, C, D, E gallons. How do
# you measure in the shortest amount of "operations / actions" the amount X ?
from collections import defaultdict


class BucketSolverGeneral:
    def __init__(self, jugs: list[int]) -> None:
        self.jug_max_vals = jugs
        self.visited = defaultdict(lambda: False)

    def buckets_recursive(self, jugs: list[int], val: int) -> bool:
        if sum(jugs) == val:
            print('final jugs', jugs)
            return True

        if not self.visited[(jugs_tuple := tuple(jugs))]:
            self.visited[jugs_tuple] = True

            # empty each jug
            for index, jug in enumerate(jugs):
                prev_val = jugs[index]
                jugs[index] = 0

                if self.buckets_recursive(jugs, val):
                    return True

                jugs[index] = prev_val

            # fill each jug
            for index, jug in enumerate(jugs):
                prev_val = jugs[index]
                jugs[index] = self.jug_max_vals[index]

                if self.buckets_recursive(jugs, val):
                    return True

                jugs[index] = prev_val

            # fill jug j from jug i
            for i, _ in enumerate(jugs):
                j = i + 1
                while j < len(jugs):
                    prev_jug_i = jugs[i]
                    prev_jug_j = jugs[j]

                    new_jug_i = jugs[i] - min(jugs[i], (self.jug_max_vals[j] - jugs[j]))
                    new_jug_j = jugs[j] + min(self.jug_max_vals[j] - jugs[j], jugs[i])

                    jugs[i] = new_jug_i
                    jugs[j] = new_jug_j

                    if self.buckets_recursive(jugs, val):
                        return True

                    jugs[i] = prev_jug_i
                    jugs[j] = prev_jug_j

                    j += 1

            # fill jug i from jug j
            for i, _ in enumerate(jugs):
                j = i + 1
                while j < len(jugs):
                    prev_jug_i = jugs[i]
                    prev_jug_j = jugs[j]

                    new_jug_j = jugs[j] - min(jugs[j], (self.jug_max_vals[i] - jugs[i]))
                    new_jug_i = jugs[i] + min(self.jug_max_vals[i] - jugs[i], jugs[j])

                    jugs[i] = new_jug_i
                    jugs[j] = new_jug_j

                    if self.buckets_recursive(jugs, val):
                        return True

                    jugs[i] = prev_jug_i
                    jugs[j] = prev_jug_j

                    j += 1

        else:
            return False


buckets = BucketSolverGeneral([5, 3, 2, 1, 10, 4])
buckets.buckets_recursive([0, 0, 0, 0, 0, 0], 20)
print(buckets.visited)
