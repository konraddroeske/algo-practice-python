def search_matrix(matrix: list[list[int]], target: int) -> bool:
    rows = len(matrix)

    if rows < 1:
        return False

    cols = len(matrix[0])

    if cols < 1:
        return False

    if target < matrix[0][0] or target > matrix[rows - 1][cols - 1]:
        return False

    top = 0
    bottom = rows - 1

    while top < bottom:
        row_mid = (top + bottom) // 2
        cur_row = matrix[row_mid]

        if target == cur_row[0]:
            return True
        elif cur_row[0] <= target <= cur_row[cols - 1]:
            top = row_mid
            bottom = row_mid
        elif target < cur_row[0]:
            bottom = row_mid - 1
        else:
            top = row_mid + 1

    row = matrix[top]
    left = 0
    right = cols - 1

    while left <= right:
        col_mid = (left + right) // 2

        if target == row[col_mid]:
            return True
        elif target < row[col_mid]:
            right = col_mid - 1
        else:
            left = col_mid + 1

    return False


def search_matrix_2d(matrix: list[list[int]], target: int) -> bool:
    if len(matrix) < 1:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid_index = (left + right) // 2
        mid_row = mid_index // cols
        mid_col = mid_index % cols
        mid_val = matrix[mid_row][mid_col]

        if target == mid_val:
            return True
        elif target < mid_val:
            right = mid_index - 1
        else:
            left = mid_index + 1

    return False


matrix_1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target_1 = 1
target_2 = 13
target_3 = 61

print(search_matrix_2d(matrix_1, target_1))
print(search_matrix_2d(matrix_1, target_2))
print(search_matrix(matrix_1, target_3))
