nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums_2 = [1]
nums_3 = [5, 4, -1, 7, 8]
nums_4 = [-1]
nums_5 = [-2, -1]
nums_6 = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]


def max_sum_brute_force(nums: list[int]) -> int:
    total_sum = sum(nums)

    for i, outer in enumerate(nums):
        test_sum = outer
        sub_arr = nums[i + 1:]

        for _, inner in enumerate(sub_arr):
            test_sum += inner
            total_sum = max(test_sum, total_sum)

    return total_sum


print(max_sum_brute_force(nums_1))
print(max_sum_brute_force(nums_2))


def max_sum(nums: list[int]) -> int:
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]

    return max(nums)


print(max_sum(nums_1))  # 6
print(max_sum(nums_2))  # 1


# print(max_sum(nums_3))  # 23
# print(max_sum(nums_4))  # -1
# print(max_sum(nums_5))  # -1
# print(max_sum(nums_6))  # 6

def max_sum_dp(nums: list[int]) -> int:
    dp = [0] * len(nums)

    for i, num in enumerate(nums):
        dp[i] = max(num, num + dp[i - 1])

    return max(dp)
