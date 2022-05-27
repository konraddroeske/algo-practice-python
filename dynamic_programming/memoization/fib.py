# Time: O(2^n)
# Space: O(n)

def fib(n: int) -> int:
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


# Memoization

# Time: O(n)
# Space: O(n)

def fib_dp(n: int, memo: dict[int, int]) -> int:
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib_dp(n - 1, memo) + fib_dp(n - 2, memo)
    return memo[n]


print(fib_dp(6, {}))
print(fib_dp(7, {}))
print(fib_dp(50, {}))
