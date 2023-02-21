def search_one_pass(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        cur_val = nums[mid]

        if cur_val == target:
            return mid
        elif cur_val >= nums[0]:
            if nums[0] <= target < cur_val:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if cur_val < target <= nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


nums_1 = [4, 5, 6, 7, 0, 1, 2]
target_1 = 0

print(search_one_pass(nums_1, target_1))

nums_2 = [4, 5, 6, 7, 0, 1, 2]
target_2 = 4

print(search_one_pass(nums_2, target_2))

nums_3 = [1]
target_3 = 0

print(search_one_pass(nums_3, target_3))

nums_4 = [3, 1]
target_4 = 1

print(search_one_pass(nums_4, target_4))
