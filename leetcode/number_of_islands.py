grid_1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid_2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


class Solution:
    def convert_island(self, row: int, col: int, grid: list[list[str]]) -> bool:
        # Stop recursion when position is equal "0"
        if grid[row][col] == "0":
            return True

        if grid[row][col] != "0":
            grid[row][col] = "0"

        # up
        if row - 1 >= 0 and grid[row - 1][col] != "0":
            if self.convert_island(row - 1, col, grid):
                return True

        # down
        if row + 1 < len(grid) and grid[row + 1][col] != "0":
            if self.convert_island(row + 1, col, grid):
                return True

        # right
        if col + 1 < len(grid[row]) and grid[row][col + 1] != "0":
            if self.convert_island(row, col + 1, grid):
                return True

        # left
        if col - 1 >= 0 and grid[row][col - 1] != "0":
            if self.convert_island(row, col - 1, grid):
                return True

    def num_islands(self, grid: list[list[str]]) -> int:
        counter = 0
        # Iterate until first "1" is found, use DFS to convert all 1s to "0" and add to counter
        # Repeat until full array is converted
        for row, _ in enumerate(grid):
            for col, _ in enumerate(grid[row]):
                if grid[row][col] == "1":
                    counter += 1
                    self.convert_island(row, col, grid)

        return counter


solution = Solution()

print(solution.num_islands(grid_1))
print(solution.num_islands(grid_2))
