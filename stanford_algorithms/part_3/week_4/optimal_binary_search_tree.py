def min_avg_search_time(keys: list[float]) -> list[list[float]]:
    n = len(keys)
    results_arr = [[0 for _ in range(n)] for _ in range(n)]

    for s_index in range(n):
        for i_index in range(n):
            if i_index > n - 1:
                break

            sub_problems = []

            for r_index in range(i_index, (i_index + 1) + s_index):
                if i_index + s_index > n - 1:
                    p_k = sum(key for key in keys[i_index:])
                else:
                    p_k = sum(key for key in keys[i_index : (i_index + 1) + s_index])

                try:
                    left_tree = results_arr[i_index][r_index - 1]
                except IndexError:
                    left_tree = 0

                try:
                    right_tree = results_arr[r_index + 1][i_index + s_index]
                except IndexError:
                    right_tree = 0

                sub_problems.append(p_k + left_tree + right_tree)

            try:
                min_val = min(sub_problems)
                results_arr[i_index][i_index + s_index] = min_val
            except (ValueError, IndexError):
                continue

    return results_arr


bst_input = [0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25]


final = min_avg_search_time(bst_input)

for row in final:
    print(row)
