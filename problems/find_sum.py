given_array = [1, 4, 3, 2, 10]


def find_sum(arr: list) -> int:
    total = 0  # O(1)
    for i in arr:  # O(1)
        total += i  # O(1)
    return total  # O(1)


# T = O(1) + n * O(1) + O(1)


def find_sum_2d(array_2d: list[list[int]]) -> int:
    total = 0  # O(1)
    for row in array_2d:
        for i in row:  # O(n^2)
            total += i  # O(1)

    return total  # O(1)
