# Merge Sort

test_arr = [2, 6, 5, 1, 4, 4, 4, 3]


def merge_sort(arr: list) -> None:
    # set condition to stop recursion of length greater than one
    if len(arr) > 1:
        # split array into left and right arr
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        # recursively split until split into single element arrays
        merge_sort(left_arr)
        merge_sort(right_arr)

        # track indexes of left, right, and parent arr
        i = 0  # left index
        j = 0  # right index
        k = 0  # merged index

        # compare left arr to right arr, update parent arr until left or right is exhausted
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1

            # increment index of parent arr
            k += 1

        # if not exhausted, iterate through left arr and assign to parent
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # if not exhausted, iterate through right arr and assign to parent
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


merge_sort(test_arr)
print(test_arr)
