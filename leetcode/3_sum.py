nums_1 = [-1, 0, 1, 2, -1, -4]
nums_2 = []
nums_3 = [0]


def three_sum(nums: list[int]) -> list[list[int]]:
    hash_map = {num: i for i, num in enumerate(nums)}
    results = []

    for i, outer in enumerate(nums):
        for j, inner in enumerate(nums[i + 1 :]):
            complement = -(outer + inner)

            third_index = hash_map.get(complement)

            if third_index and third_index != i and third_index != j:
                results.append([outer, inner, complement])

    return results


three_sum(nums_1)
three_sum(nums_2)
three_sum(nums_3)
