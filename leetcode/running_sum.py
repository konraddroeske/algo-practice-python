def running_sum(nums: list[int]) -> list[int]:
    for index, num in enumerate(nums):
        if index == 0:
            continue
        else:
            nums[index] += nums[index - 1]

    return nums


input_1 = [1, 2, 3, 4]
input_2 = [1, 1, 1, 1, 1]
input_3 = [3, 1, 2, 10, 1]

print(running_sum(input_1))
print(running_sum(input_2))
print(running_sum(input_3))
