def number_of_islands(grid: list[list[str]]) -> int:
    # iterate through grid
    # if "1", then use dfs and convert to "x", add to counter until fully
    # traversed
    counter = 0

    def dfs(y: int, x: int) -> None:
        nonlocal grid

        if grid[y][x] == "1":
            grid[y][x] = "x"

        # up
        if y > 0 and grid[y - 1][x] == "1":
            dfs(y - 1, x)

        # down
        if y + 1 < len(grid) and grid[y + 1][x] == "1":
            dfs(y + 1, x)

        # left
        if x > 0 and grid[y][x - 1] == "1":
            dfs(y, x - 1)

        # right
        if x + 1 < len(grid[y]) and grid[y][x + 1] == "1":
            dfs(y, x + 1)

    for row_index, row in enumerate(grid):
        for col_index, element in enumerate(row):
            if element == "1":
                dfs(row_index, col_index)
                counter += 1

    # raise NotImplemented
    return counter


grid_1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

print(number_of_islands(grid_1))

grid_2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print(number_of_islands(grid_2))
