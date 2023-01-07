# we have 2 buckets for water, first one can fill 5 gallons, second 3 gallons.
# How can we measure 2 gallons, by using only these two buckets?
#
# Solution: Fill the 5 gallon, to the top, and keep the 3 gallon empty. From the
# 5 gallon, transfer to the 3 gallon, until it fills to the top.
# now, the 3 gallon will be completely full, and the 5 gallon will have only 2
# gallons left. We did it :)
#
# How do we measure 7 gallons?
# Easy :)
# once you have calculated the 2 gallons from the previous case, empty the 3
# gallon, transfer the left over 2 gallons, from the 5 gallon bucket to the 3
# gallon bucket, and once you have completely emptied the 5 gallon, fill it to
# the top.What you have left is, 5 gallons completely full. and the 3 gallon
# bucket contains 2 gallons.
# 5+2=7 :)
#
# Now tell me, how do we calculate 6 gallons? or 1 gallon? or 4 gallons?
#
# can you write a program? :)
#
# and if this is very easy for you, what if we have arbitrary number of buckets,
# lets say N=5 buckets, which can be filled with A, B, C, D, E gallons. How do
# you measure in the shortest amount of "operations / actions" the amount X ?


class BucketSolver:
    def __init__(self, jug_1_max: int = 5, jug_2_max: int = 3) -> None:
        self.jug_1_max = jug_1_max
        self.jug_2_max = jug_2_max
        self.visited = [[False for _ in range(self.jug_2_max + 1)] for _ in
                        range(self.jug_1_max + 1)]

    def buckets_recursive(self, jug_1: int, jug_2: int, val: int) -> bool:
        if jug_1 + jug_2 == val or jug_1 == val or jug_2 == val:
            print(jug_1, jug_2)
            return True

        if not self.visited[jug_1][jug_2]:
            self.visited[jug_1][jug_2] = True

            return (
                # empty jug 1
                    self.buckets_recursive(0, jug_2, val) or
                    # empty jug 2
                    self.buckets_recursive(jug_1, 0, val) or
                    # fill jug 1
                    self.buckets_recursive(self.jug_1_max, jug_2, val) or
                    # fill jug 2
                    self.buckets_recursive(jug_1, self.jug_2_max, val) or
                    # fill jug 2 from jug 1
                    self.buckets_recursive(
                        jug_1 - min(jug_1, (self.jug_2_max - jug_2)),
                        jug_2 + min(self.jug_2_max - jug_2, jug_1),
                        val) or
                    # fill jug 1 from jug 2
                    self.buckets_recursive(
                        jug_1 + min(self.jug_1_max - jug_1, jug_2),
                        jug_2 - min(jug_2, (self.jug_1_max - jug_1)),
                        val)
            )
        else:
            return False


# def find_value(val: int) -> None:
#     buckets_recursive(0, 0, val)

buckets = BucketSolver(5, 3)
buckets.buckets_recursive(0, 0, 6)
print(buckets.visited)
