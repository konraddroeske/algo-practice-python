from collections import defaultdict
from dataclasses import dataclass

from tqdm import tqdm


@dataclass(repr=True)
class Item:
    value: int  # v_i
    size: int  # w_i


# capacity: int # W


with open("knapsack_input_part_2.txt") as f:
    input_items = []

    for index, line in enumerate(f):
        vals = [int(x) for x in line.split()]

        if index == 0:
            input_total_capacity = vals[0]
            input_total_items = vals[1]
        else:
            input_items.append(Item(value=vals[0], size=vals[1]))


def knapsack_problem(items: list[Item], total_capacity: int) -> int:
    results = [[0 for _ in range(total_capacity + 1)] for _ in range(len(items) + 1)]
    max_value = 0

    # Build 2D Array
    for index, item in enumerate(items, 1):
        for capacity in range(total_capacity + 1):
            case_1 = results[index - 1][capacity]
            case_2 = results[index - 1][capacity - item.size] + item.value

            if item.size > capacity:
                results[index][capacity] = case_1
                max_value = max(max_value, case_1)
            else:
                max_case = max(case_1, case_2)
                results[index][capacity] = max_case
                max_value = max(max_value, max_case)

    # print(results)

    return max_value


def knapsack_problem_optimized(items: list[Item], total_capacity: int) -> int:
    prev_row = [0 for _ in range(total_capacity + 1)]
    max_value = 0

    # Build 2D Array
    for index, item in tqdm(enumerate(items, 1)):
        new_row = [0 for _ in range(total_capacity + 1)]

        for capacity in range(total_capacity + 1):

            case_1 = prev_row[capacity]
            case_2 = prev_row[capacity - item.size] + item.value

            if item.size > capacity:
                new_row[capacity] = case_1
                max_value = max(max_value, case_1)
            else:
                max_case = max(case_1, case_2)
                new_row[capacity] = max_case
                max_value = max(max_value, max_case)

        prev_row = new_row

    # print(prev_row)

    return max_value


items_test = [
    Item(value=3, size=4),
    Item(value=2, size=3),
    Item(value=4, size=2),
    Item(value=4, size=3),
]
total_capacity_test = 6

print(knapsack_problem(items_test, total_capacity_test))
print(knapsack_problem_optimized(items_test, total_capacity_test))


# print(knapsack_problem(input_items, input_total_capacity))
# 2493893

print(knapsack_problem_optimized(input_items, input_total_capacity))
# 4243395
