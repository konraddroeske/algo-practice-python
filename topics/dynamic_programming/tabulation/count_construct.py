target_1 = "abcdef"
sub_strings_1 = ["ab", "abc", "cd", "def", "abcd"]

target_2 = "skateboard"
sub_strings_2 = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]

target_3 = "enterapotentpot"
sub_strings_3 = ["a", "p", "ent", "enter", "ot", "o", "t"]

target_4 = "purple"
sub_strings_4 = ["purp", "p", "ur", "le", "purpl"]


# Find number of ways a word can be constructed using word bank

# m = target
# n = word bank
# Time: O(m * n * m)
# Loop through target, loop through word bank, find index
# Space: O(m)

def count_construct(
        target: str,
        word_bank: list[str],
) -> int:
    table = [0] * (len(target) + 1)
    table[0] = 1

    for index, cur_val in enumerate(table):
        if cur_val:
            for word in word_bank:
                try:
                    target_sliced = target[index:index + len(word)]

                    if word == target_sliced:
                        table[index + len(word)] += cur_val
                except ValueError:
                    continue

    return table[len(target)]


print(count_construct(target_1, sub_strings_1))
print(count_construct(target_2, sub_strings_2))
print(count_construct(target_3, sub_strings_3))
print(count_construct(target_4, sub_strings_4))
