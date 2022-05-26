# b_1 = [1, 2, 3, 4]
# a_1 = [1, 2, 3, 4, 5, 6, 7, 8]

b_1 = [1, 3]
a_1 = [2]


# Use binary search to find the median
# If even, find two middle numbers and divide by 2

def find_median(a: list[int], b: list[int]) -> float:
    total = len(a) + len(b)
    half = total // 2

    # Use the smaller list for pointers
    if len(b) < len(a):
        a, b = b, a

    left_p = 0
    right_p = len(a) - 1

    while True:
        a_middle = (left_p + right_p) // 2
        b_middle = half - a_middle - 2

        a_left_end = a[a_middle] if a_middle >= 0 else float("-infinity")
        a_right_start = a[a_middle + 1] if (a_middle + 1) < len(a) else float("infinity")

        b_left_end = b[b_middle] if b_middle >= 0 else float("-infinity")
        b_right_start = b[b_middle + 1] if (b_middle + 1) < len(b) else float("infinity")

        if a_left_end <= b_right_start and b_left_end <= a_right_start:
            if total % 2:
                return min(a_right_start, b_right_start)

            left_max = max(a_left_end, b_left_end)
            right_max = min(a_right_start, b_right_start)

            return (left_max + right_max) / 2

        elif a_left_end > b_right_start:
            right_p = a_middle - 1
        else:
            left_p = a_middle + 1


print(find_median(a_1, b_1))
