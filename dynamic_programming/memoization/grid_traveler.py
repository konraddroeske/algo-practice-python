# Can only move right or down

# Time: O(m * n)
# Space: O(n + m)

def grid_traveler(rows: int, cols: int, memo: dict[tuple[int, int], int]) -> int:
    if (rows, cols) in memo:
        return memo[(rows, cols)]

    if rows == 0 or cols == 0:
        return 0

    if rows == 1 and cols == 1:
        return 1

    # go down, reduce row by one
    # go right, reduce cols by one
    memo[(rows, cols)] = grid_traveler(rows - 1, cols, memo) + \
                         grid_traveler(rows, cols - 1, memo)

    return memo[(rows, cols)]


print(grid_traveler(3, 3, {}))
print(grid_traveler(6, 6, {}))
print(grid_traveler(18, 18, {}))
