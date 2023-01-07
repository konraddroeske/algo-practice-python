# get sorted arr and element to find
# start of 0, end of len(arr) - 1
# while start <= end
# find midpoint, start + (end - start) // 2
# if midpoint val is equal to ele, return index
# elif if midpoint val is less ele, set start to midpoint + 1
# else set star to midpoint - 1
from typing import Optional


def binary_search(arr: list, ele: int) -> Optional[int]:
    start = 0
    end = len(arr) - 1

    while start <= end:
        midpoint = start + (end - start) // 2
        val = arr[midpoint]

        if val == ele:
            return midpoint
        elif ele < val:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return None


test_arr = [1, 3, 4, 5, 7, 10, 11]

print(binary_search(test_arr, 4))
print(binary_search(test_arr, 11))
