def spiral_matrix_recursion(matrix: list[list[int]]) -> list[int]:
    cur_y = 0
    cur_x = 0
    result = []
    visited = set()

    result.append(matrix[0][0])
    visited.add((0, 0))

    len_y = len(matrix)
    len_x = len(matrix[0])

    def move(y: int, x: int, dir_y: int, dir_x: int) -> tuple[int, int]:
        cur_val = matrix[y][x]
        result.append(cur_val)
        visited.add((y, x))

        new_y = y + dir_y
        new_x = x + dir_x

        if (new_y, new_x) in visited:
            return y, x

        if new_y < 0 or new_y >= len_y:
            return y, x

        if new_x < 0 or new_x >= len_x:
            return y, x

        return move(new_y, new_x, dir_y, dir_x)

    while len(result) < len_x * len_y:
        if cur_x + 1 < len_x and (cur_y, cur_x + 1) not in visited:
            cur_y, cur_x = move(cur_y, cur_x + 1, 0, 1)

        if cur_y + 1 < len_y and (cur_y + 1, cur_x) not in visited:
            cur_y, cur_x = move(cur_y + 1, cur_x, 1, 0)

        if cur_y - 1 >= 0 and (cur_y - 1, cur_x) not in visited:
            cur_y, cur_x = move(cur_y - 1, cur_x, -1, 0)

        if cur_x - 1 >= 0 and (cur_y, cur_x - 1) not in visited:
            cur_y, cur_x = move(cur_y, cur_x - 1, 0, -1)

    return result


def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    result = []
    len_y = len(matrix)
    len_x = len(matrix[0])

    top = 0
    bottom = len_y - 1
    left = 0
    right = len_x - 1

    while top <= bottom and left <= right:
        for x in range(left, right + 1):
            result.append(matrix[top][x])

        top += 1

        for y in range(top, bottom + 1):
            result.append(matrix[y][right])

        right -= 1

        if top <= bottom:
            for x in reversed(range(left, right + 1)):
                result.append(matrix[bottom][x])

            bottom -= 1

        if left <= right:
            for y in reversed(range(top, bottom + 1)):
                result.append(matrix[y][left])

            left += 1

    return result


print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
