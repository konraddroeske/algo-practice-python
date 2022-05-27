from typing import Optional

target_1 = 7
vals_1 = [5, 3, 4, 7]

target_2 = 300
vals_2 = [7, 14]

target_3 = 8
vals_3 = [2, 3, 5]


# m = target sum
# n = array length

# tree height: m = target sum / 1 (worst case)
# time: O(n ^ m)
# n branches for m levels
# space: O(n)

def how_sum_bf(
        target_sum: int,
        numbers: list[int],
) -> Optional[list[int]]:
    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum_bf(remainder, numbers)

        if remainder_result is not None:
            return remainder_result + [num]

    return None


# print(how_sum_bf(target_1, vals_1))

# time: O(n * m)
# space: O(m ^ 2)

def how_sum_dp(
        target_sum: int,
        numbers: list[int],
        memo: dict[int, Optional[list[int]]]
) -> Optional[list[int]]:
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        memo[remainder] = how_sum_dp(remainder, numbers, memo)

        if memo[remainder] is not None:
            return memo[remainder] + [num]

    memo[target_sum] = None
    return None


print(how_sum_dp(target_1, vals_1, {}))
print(how_sum_dp(target_2, vals_2, {}))
print(how_sum_dp(target_3, vals_3, {}))
