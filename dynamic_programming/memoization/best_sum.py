from typing import Optional

target_1 = 7
vals_1 = [5, 3, 4, 7]

target_2 = 8
vals_2 = [2, 3, 5]

target_3 = 100
vals_3 = [1, 2, 5, 25]


# Brute Force
# time = O(n ^ m)
# branching factor = n, height of tree = m

# space = O(m ^ 2)
# stack depth is m
# in each stack frame, we store an array

# Dynamic Programming
# time = O(m * n)
# space = O(m ^ 2)

def best_sum(
        target_sum: int,
        numbers: list[int],
        memo: dict[int, Optional[list[int]]]) \
        -> Optional[list[int]]:
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers, memo)

        if remainder_combination is not None:
            combination = remainder_combination + [num]

            if shortest_combination is None \
                    or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return shortest_combination


print(best_sum(target_1, vals_1, {}))
print(best_sum(target_2, vals_2, {}))
print(best_sum(target_3, vals_3, {}))
