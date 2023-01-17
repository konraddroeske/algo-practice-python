def unique_paths(m: int, n: int) -> int:
    result = [[0 for _ in range(n)] for _ in range(m)]

    for y_index, y_value in enumerate(result):
        for x_index, x_value in enumerate(y_value):
            if y_index == 0 or x_index == 0:
                result[y_index][x_index] = 1
                continue

            top_val = result[y_index - 1][x_index]
            left_val = result[y_index][x_index - 1]
            result[y_index][x_index] = top_val + left_val


    return result[-1][-1]


print(unique_paths(3, 2))
print(unique_paths(3, 7))
