# input: array of length n, containing ints
# output: number of inversions (pairs of indices with i < j, and A[i] > A[j])

arr_1 = [1, 3, 5, 2, 4, 6]
arr_2 = [5, 1]
arr_3 = [6, 5, 4, 3, 2, 1]

integer_file = open("integer_arr.txt", "r")
arr_4 = integer_file.read().split("\n")
arr_4 = [int(num) for num in arr_4]

# print(arr_4)

# inversions = (3, 2), (5, 2), (5, 4), etc...

# What is the largest number of inversion that a 6-element array can have?
# n * (n - 1) / 2

# Brute Force
# Double For Loop - check each pair individually
# O(n ^ 2)

# Divide and Conquer
# Inversion is (i, j) w/ i < j:

# can we counted recursively
# left if i and j <= n / 2
# right if i and j > n / 2

# need separate subroutine for these
# split if i <= n / 2 < j


def merge_and_count_split_inv(
    left: list[int], right: list[int]
) -> tuple[list[int], int]:
    output = []

    i = 0
    j = 0
    inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
            inversions += len(left) - i

    output += left[i:]
    output += right[j:]

    return output, inversions


def sort_and_count(a: list[int]) -> tuple[list[int], int]:
    if len(a) == 1:
        return a, 0

    mid = len(a) // 2

    b = a[:mid]
    c = a[mid:]

    (b, x) = sort_and_count(b)
    (c, y) = sort_and_count(c)
    (a, z) = merge_and_count_split_inv(b, c)

    return a, x + y + z


print(sort_and_count(arr_1))
print(sort_and_count(arr_2))
print(sort_and_count(arr_3))
print(sort_and_count(arr_4))
