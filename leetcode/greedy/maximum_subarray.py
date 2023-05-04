def max_subarray(nums: list[int]) -> int:
    cur_sum = nums[0]
    max_sub = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]
        cur_sum = max(cur_sum + num, num)
        max_sub = max(max_sub, cur_sum)

    return max_sub


nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums_2 = [1]
nums_3 = [5, 4, -1, 7, 8]

print(max_subarray(nums_1))
print(max_subarray(nums_2))
print(max_subarray(nums_3))
