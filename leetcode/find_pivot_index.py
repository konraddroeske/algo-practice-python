def pivot_index(nums: list[int]) -> int:
    left_sum = 0
    right_sum = sum(nums)

    for index, num in enumerate(nums):
        right_sum -= nums[index]

        if index > 0:
            left_sum += nums[index - 1]

        if left_sum == right_sum:
            return index

    return -1


input_1 = [1, 7, 3, 6, 5, 6]
input_2 = [1, 2, 3]
input_3 = [2, 1, -1]

print(pivot_index(input_1))
print(pivot_index(input_2))
print(pivot_index(input_3))
