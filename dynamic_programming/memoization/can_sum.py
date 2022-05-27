target_1 = 7
vals_1 = [5, 3, 4, 7]

target_2 = 300
vals_2 = [7, 14]


# m = target sum
# n = array length

# worst case height = m
# time = O(n ^ m)
# space = O(m)
# n branches for m levels

def can_sum_bf(target_sum: int, numbers: list[int]) -> bool:
    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num

        if can_sum_bf(remainder, numbers) is True:
            return True

    return False


# time = O(m * n)
# space = O(m)

def can_sum_dp(target_sum: int, numbers: list[int], memo: dict[int, bool]) -> bool:
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num

        memo[remainder] = can_sum_dp(remainder, numbers, memo)

        if memo[remainder] is True:
            return True

    memo[target_sum] = False
    return memo[target_sum]


print(can_sum_dp(target_1, vals_1, {}))
print(can_sum_dp(target_2, vals_2, {}))
