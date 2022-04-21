from typing import Optional


def get_pos(board: list[list[str]], target: str) -> (int, int):
    for row, _ in enumerate(board):
        for col, _ in enumerate(board[row]):
            if board[row][col] == target:
                return row, col

    raise ValueError("Start cannot be None")


board_1 = [
    [".", "#", ".", "S", ".", "."],
    [".", "#", ".", ".", ".", "."],
    [".", "#", "#", "#", ".", "."],
    [".", ".", ".", "#", ".", "."],
    ["F", ".", ".", "#", ".", "."],
]

start_1 = get_pos(board_1, "S")
finish_1 = get_pos(board_1, "F")

print('start', start_1)
print('finish', finish_1)


def get_neighbours(board: list[list[str]], cur_pos: tuple[int, int]) \
        -> list[tuple[int, int]]:
    row, col = cur_pos

    neighbours = []

    # up
    if row - 1 >= 0 and board[row - 1][col] not in ("#", "P", "S"):
        neighbours.append((row - 1, col))

    # down
    if row + 1 < len(board) and board[row + 1][col] not in ("#", "P", "S"):
        neighbours.append((row + 1, col))

    # right
    if col + 1 < len(board[row]) and board[row][col + 1] not in ("#", "P", "S"):
        neighbours.append((row, col + 1))

    # left
    if col - 1 >= 0 and board[row][col - 1] not in ("#", "P", "S"):
        neighbours.append((row, col - 1))

    return neighbours


def bfs(board: list[list[str]], start_pos: tuple[int, int]) \
        -> list[list[Optional[tuple[int, int]]]]:
    q = [start_pos]
    paths = [[None for _ in row] for row in board]

    while len(q) > 0:
        cur_pos = q.pop(0)
        cur_row, cur_col = cur_pos

        if board[cur_row][cur_col] == "F":
            return paths

        board[cur_row][cur_col] = "P"

        for next_pos in get_neighbours(board, cur_pos):
            next_row, next_col = next_pos
            paths[next_row][next_col] = cur_pos

            q.append(next_pos)


def get_shortest_path(paths: list[list[Optional[tuple[int, int]]]],
                      start: tuple[int, int],
                      finish: tuple[int, int]) \
        -> list[tuple[int, int]]:
    cur_node = finish
    shortest = [cur_node]

    while cur_node is not None:
        cur_row, cur_col = cur_node
        prev_node = paths[cur_row][cur_col]

        if prev_node == start:
            return shortest[::-1]

        prev_row, prev_col = prev_node
        shortest.append(prev_node)

        cur_node = paths[prev_row][prev_col]

    return []


result = bfs(board_1, start_1)

if result is None:
    print('could not find solution')
else:
    for row in result:
        print(row)
    print('\n')

    shortest_path = get_shortest_path(result, start_1, finish_1)

    print('shortest path', shortest_path)
