# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]
from typing import Optional


# 1 - Brute Force
# Two For Loops, with nested one starting ahead

# Time Complexity = n^2

def two_sum(nums: list[int], target: int) -> Optional[list[int]]:
    for i, _ in enumerate(nums):
        for j, _ in enumerate(nums[i + 1:]):
            k = i + j + 1
            if nums[i] + nums[k] == target:
                return [i, k]

    return []


input_1 = [2, 7, 11, 15]
target_1 = 9

print(two_sum(input_1, target_1))

input_2 = [3, 2, 4]
target_2 = 6

print(two_sum(input_2, target_2))


# 2 - Memoization - 1 Pass

# Time Complexity = n

def two_sum_one_pass(nums: list[int], target: int) -> list[int]:

    if len(nums) < 2:
        return []

    hash_table = {}

    for i, val in enumerate(nums):
        complement = target - val

        if complement in hash_table:
            return [hash_table[complement], i]

        hash_table[val] = i

    return []


input_1 = [2, 7, 11, 15]
target_1 = 9

print(two_sum_one_pass(input_1, target_1))

input_2 = [3, 2, 4]
target_2 = 6

print(two_sum_one_pass(input_2, target_2))
