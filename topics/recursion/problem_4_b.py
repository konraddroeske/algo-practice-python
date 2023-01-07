# and if this is very easy for you, what if we have arbitrary number of buckets,
# lets say n=5 buckets, which can be filled with a, b, c, d, e gallons. how do
# you measure in the shortest amount of "operations / actions" the amount x ?
from collections import defaultdict


class BucketSolverGeneral:
    def __init__(self, jugs: list[int]) -> None:
        self.jug_max_vals = jugs
        self.visited = defaultdict(lambda: False)

    def buckets_recursive(self, jugs: list[int], val: int, path: list[str]) \
            -> bool:
        if sum(jugs) == val:
            print('final jugs', jugs)
            print('final path', path)
            return True

        if not self.visited[(jugs_tuple := tuple(jugs))]:
            self.visited[jugs_tuple] = True
            # path.append(jugs_tuple)

            # empty each jug
            for index, jug in enumerate(jugs):
                prev_val = jugs[index]
                jugs[index] = 0
                path.append(f'Empty jug: {index}')

                if self.buckets_recursive(jugs, val, path):
                    return True

                jugs[index] = prev_val
                path.pop()

            # fill each jug
            for index, jug in enumerate(jugs):
                prev_val = jugs[index]
                jugs[index] = self.jug_max_vals[index]
                path.append(f'Fill jug: {index}')

                if self.buckets_recursive(jugs, val, path):
                    return True

                jugs[index] = prev_val
                path.pop()

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

                    path.append(f'Fill jug {j} from jug {i}')

                    if self.buckets_recursive(jugs, val, path):
                        return True

                    jugs[i] = prev_jug_i
                    jugs[j] = prev_jug_j
                    path.pop()

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

                    path.append(f'Fill jug {i} from jug {j}')

                    if self.buckets_recursive(jugs, val, path):
                        return True

                    jugs[i] = prev_jug_i
                    jugs[j] = prev_jug_j
                    path.pop()

                    j += 1

        else:
            return False


# buckets = BucketSolverGeneral([5, 3, 2, 1, 10, 4])
# buckets.buckets_recursive([0, 0, 0, 0, 0, 0], 20, [])
# print(buckets.visited)
# print(len(buckets.visited))

buckets = BucketSolverGeneral([5, 3])
buckets.buckets_recursive([0, 0], 6, [])
print(buckets.visited)
