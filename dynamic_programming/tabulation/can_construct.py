target_1 = "abcdef"
sub_strings_1 = ["ab", "abc", "cd", "def", "abcd"]

target_2 = "skateboard"
sub_strings_2 = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]


# m = target
# n = word bank

# time = O(m * n * m) = O(m^2 * n)
# loop through target, loop through words, loop to find index
# space = O(m)
# list size of target with boolean


def can_construct(
        target: str,
        word_bank: list[str],
) -> bool:
    table = [False] * (len(target) + 1)
    table[0] = True

    for index, table_val in enumerate(table):
        if table_val:
            for word in word_bank:
                try:
                    word_index = target.index(word, index)

                    if word_index == index:
                        table[index + len(word)] = True

                except ValueError:
                    continue

    return table[len(target)]


print(can_construct(target_1, sub_strings_1))
print(can_construct(target_2, sub_strings_2))
