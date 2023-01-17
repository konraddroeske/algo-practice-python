def unique_paths(m: int, n: int) -> int:
    result = [[1 for _ in range(n)] for _ in range(m)]

    for row in range(1, m):
        for col in range(1, n):
            result[row][col] = result[row - 1][col] + result[row][col - 1]

    return result[-1][-1]


print(unique_paths(3, 2))
print(unique_paths(3, 7))
