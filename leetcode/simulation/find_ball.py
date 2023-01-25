def find_ball(grid: list[list[int]]) -> list[int]:
    len_y = len(grid) - 1
    len_x = len(grid[0]) - 1
    result = []

    for ball in range(len_x + 1):
        pos_y = 0
        pos_x = ball

        while pos_y <= len_y:
            cur_pos = grid[pos_y][pos_x]
            # go right
            if cur_pos == 1:
                if pos_x + 1 > len_x or grid[pos_y][pos_x + 1] == -1:
                    break
                else:
                    pos_y += 1
                    pos_x += 1

            # go left
            if cur_pos == -1:
                if pos_x - 1 < 0 or grid[pos_y][pos_x - 1] == 1:
                    break
                else:
                    pos_y += 1
                    pos_x -= 1

        if pos_y > len_y:
            result.append(pos_x)
        else:
            result.append(-1)

    return result


print(
    find_ball(
        [
            [1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1],
            [1, 1, 1, 1, -1],
            [-1, -1, -1, -1, -1],
        ]
    )
)
print(find_ball([[-1]]))
print(
    find_ball(
        [
            [1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
            [1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
        ]
    )
)
