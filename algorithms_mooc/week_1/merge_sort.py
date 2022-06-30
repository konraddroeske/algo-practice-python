# input: array of n numbers
# output: same numbers, sorted in increasing order

nums_1 = [5, 4, 1, 8, 7, 2, 6, 3]


def merge_sort(arr: list[int]) -> list[int]:
    n = len(arr)

    # base case
    if n < 2:
        return arr

    output = []
    mid = n // 2

    # 2 recursive calls
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = 0  # 1 operation
    j = 0  # 1 operation

    while i < len(left) and j < len(right):  # n operations
        if left[i] <= right[j]:  # 1 operation
            output.append(left[i])  # 1 operation
            i += 1  # 1 operation
        else:
            output.append(right[j])
            j += 1

    # end cases
    output += left[i:]  # n operations
    output += right[j:]  # n operations

    return output

    # Simplify to max 6n operations per merge


print(merge_sort(nums_1))

# Analysis

# Levels: log n + 1

# At level j, how many sub problems? 2 ^ j
# Each of size? n / (2 ^ j)
# Amount of work done at each level: Merge Subroutine - 6n

# number of level j subproblems * subproblem size at level j * work per level j subproblem
# (2 ^ j) * 6 * (n / 2 ^ j) = 6n

# levels * 6n
# Time Complexity: 6n log n + 6n
