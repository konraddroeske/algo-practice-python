def min_avg_search_time(keys: list[float]) -> list[list[float]]:
    n = len(keys)
    results_arr = [[0 for _ in range(n)] for _ in range(n)]

    for s_index in range(n):
        for i_index in range(n):
            if s_index + i_index > n - 1:
                continue

            sub_problems = []

            for r_index in range(i_index, (i_index + 1) + s_index):
                p_k = sum(key for key in keys[i_index : (i_index + 1) + s_index])

                if i_index > r_index - 1:
                    left_tree = 0
                else:
                    left_tree = results_arr[i_index][r_index - 1]

                if r_index + 1 > i_index + s_index:
                    right_tree = 0
                else:
                    right_tree = results_arr[r_index + 1][i_index + s_index]

                sub_problems.append(p_k + left_tree + right_tree)

            results_arr[i_index][i_index + s_index] = min(sub_problems)

    return results_arr


bst_input = [0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25]


final = min_avg_search_time(bst_input)

for row in final:
    print(row)
