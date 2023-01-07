# initial condition: if arr less or equal one, return
# pop pivot value
# create list for smaller, larger
# recursively call quick sort

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


test_arr = [123, 3, 2, 1, 7, 2, 11, 3]

print(quick_sort(test_arr))
