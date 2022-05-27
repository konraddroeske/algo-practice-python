from typing import Optional

target_1 = 7
vals_1 = [5, 3, 4, 7]

target_2 = 8
vals_2 = [2, 3, 5]

target_3 = 100
vals_3 = [1, 2, 5, 25]


# m = target_sum
# n = numbers

# time = O(m * n * m)
# loop through m, loop through n, copy list up to length m
# space = O(m * m)
# table of size m * list of numbers up to size m (worst case)

def best_sum(
        target_sum: int,
        numbers: list[int],
) -> Optional[list[int]]:
    table: list[Optional[list[int]]] = [None] * (target_sum + 1)
    table[0] = []

    for index in range(target_sum):
        for num in numbers:

            current = table[index]

            if current is not None and index + num < len(table):
                existing_sum = table[index + num]
                new_sum = table[index] + [num]

                if existing_sum is None or len(new_sum) < len(existing_sum):
                    table[index + num] = table[index] + [num]

    return table[target_sum]


print(best_sum(target_1, vals_1))
print(best_sum(target_2, vals_2))
print(best_sum(target_3, vals_3))
