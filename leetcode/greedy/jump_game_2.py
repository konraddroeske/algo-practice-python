def jumpDP(nums: list[int]) -> int:
    total_jumps = 0
    cur_jump = 0
    max_jump = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        if i > cur_jump:
            total_jumps += 1
            cur_jump = max_jump

        max_jump = max(max_jump, num + i)

    return total_jumps


def jumpTwoPointer(nums: list[int]) -> int:
    total_jumps = 0
    l = r = 0

    while r < len(nums) - 1:
        max_jump = 0

        for i in range(l, r + 1):
            max_jump = max(max_jump, i + nums[i])

        l = r + 1
        r = max_jump
        total_jumps += 1

    return total_jumps


nums_1 = [2, 3, 1, 1, 4]
nums_2 = [2, 3, 0, 1, 4]
nums_3 = [2, 3, 0, 1, 4, 1, 1, 1, 1, 1]


print(jumpTwoPointer(nums_1))
print(jumpTwoPointer(nums_2))
print(jumpTwoPointer(nums_3))
