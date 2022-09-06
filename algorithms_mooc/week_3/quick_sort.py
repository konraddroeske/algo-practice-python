arr_1 = [4, 2, 5, 1, 8, 7, 6, 3]
arr_2 = [8, 2, 4, 5, 7, 1]

with open("quicksort_input.txt") as f:
    arr_4 = [int(x) for x in f]


def find_median(arr: list[int]) -> int:
    min_value = min(arr)
    max_value = max(arr)

    mid_value = next(
        iter(pivot for pivot in arr if pivot != min_value and pivot != max_value),
        None,
    )

    if mid_value is None:
        return min_value

    return mid_value


def choose_pivot(arr: list[int], flag: int) -> int:
    n = len(arr)

    if flag == 1:
        return 0

    if flag == 2:
        return n - 1

    first = arr[0]
    final = arr[n - 1]

    if n % 2 != 0:
        k = n // 2
        middle = arr[k]
    else:
        k = (n - 1) // 2
        middle = arr[k]

    pivot_arr = [first, middle, final]

    med = find_median(pivot_arr)

    if med == first:
        return 0
    elif med == middle:
        return k
    else:
        return n - 1


def swap(arr: list[int], first: int, second: int) -> list[int]:
    arr[first], arr[second] = arr[second], arr[first]
    return arr


def partition(arr: list[int]) -> tuple[list[int], int]:
    pivot = arr[0]
    r = len(arr)
    i = 1

    for j in range(1, r):
        if arr[j] < pivot:
            arr = swap(arr, i, j)
            i += 1

    arr = swap(arr, 0, i - 1)

    return arr, i - 1


def quick_sort(arr: list[int], flag: int) -> tuple[list[int], int]:
    n = len(arr)

    if n < 2:
        return arr, 0

    pivot_pos = choose_pivot(arr, flag)
    arr = swap(arr, 0, pivot_pos)
    arr, partition_pos = partition(arr)
    arr[:partition_pos], left = quick_sort(arr[:partition_pos], flag)
    arr[partition_pos + 1 :], right = quick_sort(arr[partition_pos + 1 :], flag)

    return arr, left + right + n - 1


# test_1 = quick_sort(arr_1, 3)
# print("test 1", test_1)
#
# test_2 = quick_sort(arr_2, 3)
# print("test 2", test_2)

# result_1 = quick_sort(arr_4, 1)
# print("result 1", result_1)
# 162085

# result_2 = quick_sort(arr_4, 2)
# print("result 2", result_2)
# 164123

result_3 = quick_sort(arr_4, 3)
print("result 3", result_3)
# 138382
