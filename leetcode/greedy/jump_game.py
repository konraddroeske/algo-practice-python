def can_jump(nums: list[int]) -> bool:
    max_jump = 0

    for i, num in enumerate(nums):
        if num == 0 and max_jump <= i and i != len(nums) - 1:
            return False

        max_jump = max(max_jump, num + i)

    return True


nums_1 = [2, 3, 1, 1, 4]  # true
nums_2 = [3, 2, 1, 0, 4]  # false
nums_3 = [0]  # true


print(can_jump(nums_1))
print(can_jump(nums_2))
print(can_jump(nums_3))
