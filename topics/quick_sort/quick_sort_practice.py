# initial condition: if length < 1 return arr
# get pivot from pop()
# create two array, for smaller and larger
# compare and append values from array based on pivot
# iteratively call quick sort on smaller and larger, with pivot in between


def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    smaller = []
    larger = []

    for ele in arr:
        if ele < pivot:
            smaller.append(ele)
        else:
            larger.append(ele)

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


test_arr = [5, 2, 7, 3, 2, 6, 7, 8, 21, 1]

print(quick_sort(test_arr))
