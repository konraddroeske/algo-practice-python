from typing import Optional

target_1 = "abcdef"
sub_strings_1 = ["ab", "abc", "cd", "def", "abcd", "ef", "c"]

target_2 = "skateboard"
sub_strings_2 = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]

target_3 = "enterapotentpot"
sub_strings_3 = ["a", "p", "ent", "enter", "ot", "o", "t"]

target_4 = "purple"
sub_strings_4 = ["purp", "p", "ur", "le", "purpl"]


# Return all combinations of substrings that equal target

# m = target string
# n = word bank

# time - O(n ^ m)
# space - O(n ^ m)

def all_construct(
        target: str,
        word_bank: list[str]
) -> Optional[list[list[str]]]:
    table: list[Optional[list[list[str]]]] = [None] * (len(target) + 1)
    table[0] = [[]]

    for index, vals in enumerate(table):
        if vals is not None:
            for word in word_bank:

                target_sliced = target[index:index + len(word)]

                if word == target_sliced:
                    combined = [val + [word] for val in vals]

                    if table[index + len(word)] is None:
                        table[index + len(word)] = combined
                    else:
                        table[index + len(word)] += combined

    return table[len(target)]


print(all_construct(target_1, sub_strings_1))
print(all_construct(target_2, sub_strings_2))
print(all_construct(target_3, sub_strings_3))
print(all_construct(target_4, sub_strings_4))
