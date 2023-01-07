# sort array in place
# check if arr len > 1
# split into two
# set up indices for left, right, and merged
# iterate through both until exhausted, changing array value in place
# iterate through left and right until exhausted

def merge_sort(arr: list) -> None:
    if len(arr) > 1:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]

        merge_sort(left)
        merge_sort(right)

        l_index = 0
        r_index = 0
        merged_index = 0

        while l_index < len(left) and r_index < len(right):
            if left[l_index] < right[r_index]:
                arr[merged_index] = left[l_index]
                l_index += 1
            else:
                arr[merged_index] = right[r_index]
                r_index += 1

            merged_index += 1

        while l_index < len(left):
            arr[merged_index] = left[l_index]
            l_index += 1
            merged_index += 1

        while r_index < len(right):
            arr[merged_index] = right[r_index]
            r_index += 1
            merged_index += 1


test_arr = [2, 5, 76, 1, 1, 2, 4, 5, 7, 9]

merge_sort(test_arr)

print(test_arr)
