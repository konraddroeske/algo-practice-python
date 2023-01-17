def min_cost_climbing_stairs(cost: list[int]) -> int:

    for index, step_cost in enumerate(cost):
        if index == 0 or index == 1:
            continue

        case_1 = cost[index - 1] + step_cost
        case_2 = cost[index - 2] + step_cost

        cost[index] = min(case_1, case_2)

    return min(cost[-1], cost[-2])


input_1 = [10, 15, 20]
input_2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

print(min_cost_climbing_stairs(input_1))
print(min_cost_climbing_stairs(input_2))
