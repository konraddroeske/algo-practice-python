# ...SPP.......
# ...##P.......
# .....P...##..
# #....PPPPF...

# 1. print any path
# 2. if multiple paths exist, find the shortest one
# 3.
from typing import Optional


# class Pathfinding:
#     def __init__(self, start_board: list[list[str]]) -> None:
#         self.board = start_board
#         row, col = self.get_start(self.board)
#         self.row = row
#         self.col = col

# dijkstra can be used, but that is not my point.
# some modification of dfs or bfs ?? who knows,
def get_start(board: list[list[str]]) -> (int, int):
    for row, _ in enumerate(board):
        for col, _ in enumerate(board[row]):
            if board[row][col] == "S":
                return row, col

    raise ValueError("Start cannot be None")


def print_board(board: list[list[str]]) -> None:
    for row in board:
        print(row)

    print('\n')


counter = 0


def find_path(board: list[list[str]], row: int, col: int) -> bool:
    global counter
    counter += 1

    if board[row][col] == "F":
        print_board(board)
        return True

    if board[row][col] != "S":
        board[row][col] = "P"

    # up
    if row - 1 >= 0 and board[row - 1][col] not in ("#", "P", "S"):
        if find_path(board, row - 1, col):
            return True

        board[row][col] = "."

    # down
    if row + 1 < len(board) and board[row + 1][col] not in ("#", "P", "S"):
        if find_path(board, row + 1, col):
            return True

        board[row][col] = "."

    # right
    if col + 1 < len(board[row]) and board[row][col + 1] not in ("#", "P", "S"):
        if find_path(board, row, col + 1):
            return True

        board[row][col] = "."

    # left
    if col - 1 >= 0 and board[row][col - 1] not in ("#", "P", "S"):
        if find_path(board, row, col - 1):
            return True

        board[row][col] = "."


# DFS
# Recursion in all directions until end point is found
# Backtracking to reset cells that do not lead to solution

# row, col = get_start(board)


board = [
    [".", "#", ".", "S", ".", "."],
    [".", "#", ".", ".", ".", "."],
    [".", "#", "#", "#", ".", "."],
    [".", ".", ".", ".", ".", "."],
    ["F", ".", ".", ".", ".", "."],
]

# solver = Pathfinding(board)
row, col = get_start(board)

print('row', row)
print('col', col)

result = find_path(board, row, col)

print('result', result)
print('counter', counter)
