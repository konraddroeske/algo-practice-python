def can_sum(target_sum: int, numbers: list[int]) -> bool:
    table = [False] * (target_sum + 1)
    table[0] = True

    for index in range(target_sum):
        for num in numbers:
            current = table[index]
            if current and index + num < len(table):
                table[index + num] = True

    return table[target_sum]


# Time = O(m * n)
# Space = O(m)

target_1 = 7
numbers_1 = [5, 3, 4]

target_2 = 300
numbers_2 = [7, 14]

print(can_sum(target_1, numbers_1))
print(can_sum(target_2, numbers_2))
