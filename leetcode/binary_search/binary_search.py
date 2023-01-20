def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


    return -1

nums_1 = [-1,0,3,5,9,12]
target_1 = 9

nums_2 = [-1,0,3,5,9,12]
target_2 = 2

nums_3 = [1, 12]
target_3 = 1

print(binary_search(nums_1, target_1))
print(binary_search(nums_2, target_2))
print(binary_search(nums_3, target_3))
