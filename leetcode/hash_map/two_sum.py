def two_sum(nums: list[int], target: int) -> list[int]:
    if len(nums) < 2:
        return []

    hash_table = {}

    for index, num in enumerate(nums):
        diff = target - num

        if hash_table.get(diff) is not None:
            return [index, hash_table[diff]]

        hash_table[num] = index

    return []

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
