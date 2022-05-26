# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
# intervals, and return an array of the non-overlapping intervals that cover all the
# intervals in the input.


input_1 = [[2, 6], [8, 10], [15, 18], [1, 3]]
input_2 = [[1, 4], [4, 5]]
input_3 = [[1, 4], [1, 4]]
input_4 = [[1, 4], [1, 5]]


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    merged = []

    for interval in sorted(intervals, key=lambda x: x[0]):
        # cur interval start is less or equal to prev interval end
        if merged and interval[0] <= merged[-1][1]:
            # set end to the max of cur interval end or prev interval end
            merged[-1][1] = max(interval[1], merged[-1][1])
        else:
            merged.append(interval)

    return merged


print(merge_intervals(input_1))
print(merge_intervals(input_2))
print(merge_intervals(input_3))
print(merge_intervals(input_4))
