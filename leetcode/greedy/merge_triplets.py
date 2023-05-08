def is_larger(triplet: list[int], target: list[int]) -> bool:
    for i, target_val in enumerate(target):
        if triplet[i] > target_val:
            return True

    return False


def merge_triplets(triplets: list[list[int]], target: list[int]) -> bool:
    result = set()

    for triplet in triplets:
        if is_larger(triplet, target):
            continue

        for i, target_val in enumerate(target):
            if triplet[i] == target_val:
                result.add(i)

                if len(result) == 3:
                    return True

    return False


triplets_1 = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target_1 = [2, 7, 5]
print(merge_triplets(triplets_1, target_1))
# true

triplets_2 = [[3, 4, 5], [4, 5, 6]]
target_2 = [3, 2, 5]
print(merge_triplets(triplets_2, target_2))
# false

triplets_3 = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
target_3 = [5, 5, 5]
print(merge_triplets(triplets_3, target_3))
# true
