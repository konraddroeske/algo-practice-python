from typing import Optional

target_1 = 7
vals_1 = [5, 3, 4, 7]

target_2 = 300
vals_2 = [7, 14]

target_3 = 8
vals_3 = [2, 3, 5]


# m = target sum
# n = numbers length

# Time: O(m ^ 2 * n)
# Space: O(m ^ 2)

def how_sum(
        target_sum: int,
        numbers: list[int],
) -> Optional[list[int]]:
    table: list[Optional[list[int]]] = [None] * (target_sum + 1)  # space = m
    table[0] = []

    for index in range(target_sum):  # time = m
        for num in numbers:  # time = n
            current = table[index]

            if current is not None and (index + num) < len(table):
                table[index + num] = current + [num]  # time = m, space = m

    return table[target_sum]


print(how_sum(target_1, vals_1))
print(how_sum(target_2, vals_2))
print(how_sum(target_3, vals_3))
