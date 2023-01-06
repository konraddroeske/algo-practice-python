from dataclasses import dataclass


@dataclass(repr=True)
class Item:
    value: int  # v_i
    size: int  # w_i


# capacity: int # W


with open("knapsack_input_part_2.txt") as f:
    items = []

    for index, line in enumerate(f):
        vals = [int(x) for x in line.split()]

        if index == 0:
            total_capacity = vals[0]
            total_items = vals[1]
        else:
            items.append(Item(value=vals[0], size=vals[1]))


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

    # return results
    # for index, row in enumerate(results):
    #     print(f"index {index}", row)

    # Reconstruct results
    # find max value, then work backwards
    return max_value


items_test = [
    Item(value=3, size=4),
    Item(value=2, size=3),
    Item(value=4, size=2),
    Item(value=4, size=3),
]
total_capacity_test = 6

print(knapsack_problem(items, total_capacity))
