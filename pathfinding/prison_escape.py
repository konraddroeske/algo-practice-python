# Prison Escape
#
# Robbie is a prisoner, who wants to escape.
# his location is R.
# Exit is E
# and there are guards around the prison - G.
# (you will have max 10 guards)
# matrix couold be 200x200
#
#
# 8 9
# .R.......
# .........
# ..G...G..
# .........
# G........
# ....G....
# ...**....
# ...E.....
#
# The goal is, find a path to the exit, so that, you are always the furthest away from the guards.
# So, what is the max distance, you can keep away from the guards, while reaching the exit?
#
# Output 2
#
# .R+++....
# ....+....
# ..G.+.G..
# ....++...
# G....+++.
# ....G..+.
# ...**..+.
# ...E++++.
#
#
# 8 9
# .R+++++++
# ........+
# ..G...G.+
# ........+
# G.......+
# ....G...+
# ...**...+
# ...E+++++

# Brute Force

# 1. Convert board into nodes with scores with distance to closest guard using BFS.
from typing import Union


def get_neighbours(board: list[list[str]], cur_pos: tuple[int, int, int]) \
        -> list[tuple[int, int, int]]:
    row, col, distance = cur_pos

    neighbours = []

    barriers = "*"

    # up
    if row - 1 >= 0 and board[row - 1][col] != barriers:
        neighbours.append((row - 1, col, distance + 1))

    # down
    if row + 1 < len(board) and board[row + 1][col] != barriers:
        neighbours.append((row + 1, col, distance + 1))

    # right
    if col + 1 < len(board[row]) and board[row][col + 1] != barriers:
        neighbours.append((row, col + 1, distance + 1))

    # left
    if col - 1 >= 0 and board[row][col - 1] != barriers:
        neighbours.append((row, col - 1, distance + 1))

    return neighbours


def convert_board(board: list[list[Union[str, int]]]) -> list[list[Union[str, int]]]:
    print('converting board')

    for row, _ in enumerate(board):
        for col, _ in enumerate(board[row]):
            if board[row][col] == ".":
                start_pos = (row, col, 0)
                q = [start_pos]

                while len(q) > 0:
                    cur_pos = q.pop(0)
                    cur_row, cur_col, distance = cur_pos

                    if board[cur_row][cur_col] == "G":
                        board[row][col] = distance
                        break

                    for next_pos in get_neighbours(board, cur_pos, distance + 1):
                        q.append(next_pos)

                    # distance += 1

    return board


# .R.......
# .........
# ..G...G..
# .........
# G........
# ....G....
# ...**....
# ...E.....

board_1 = [
    [".", "G", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "G", ".", ".", ".", "G", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["G", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "G", ".", ".", ".", "."],
    [".", ".", ".", "*", "*", ".", ".", ".", "."],
    [".", ".", ".", "E", ".", ".", ".", ".", "."],
]

converted_board = convert_board(board_1)

print('converted board')

for row in converted_board:
    print(row)

# 2. Use DFS, starting from most restrictive (max distance) to least (
# 1), until you can exit.

# ALT: Use Dijksta's to find the most expensive path?

# def find_max_distance_path(board: list[list[str]]) -> list[list[str]]:
#     print('find max distance path')
