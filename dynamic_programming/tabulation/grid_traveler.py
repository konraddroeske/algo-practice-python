def grid_traveler(rows: int, cols: int) -> int:
    table = [[0] * (cols + 1) for _ in range(rows + 1)]
    table[1][1] = 1

    for row, _ in enumerate(table):
        for col, _ in enumerate(table[row]):
            current = table[row][col]

            if row + 1 <= rows:
                table[row + 1][col] += current

            if col + 1 <= cols:
                table[row][col + 1] += current

    return table[rows][cols]


print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))
