target_1 = "abcdef"
sub_strings_1 = ["ab", "abc", "cd", "def", "abcd"]

target_2 = "skateboard"
sub_strings_2 = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]

target_3 = "enterapotentpot"
sub_strings_3 = ["a", "p", "ent", "enter", "ot", "o", "t"]

target_4 = "purple"
sub_strings_4 = ["purp", "p", "ur", "le", "purpl"]


# m = target length
# n = word bank length

# height of tree = m
# time: O(n^m) - n branches, m levels
# Cannot do better than exponential
# space: O(m)

def all_construct(
        target: str,
        word_bank: list[str],
        memo: dict[str, list[list[str]]]
) -> list[list[str]]:
    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []

    for word in word_bank:
        try:
            index = target.index(word)

            if index == 0:
                suffix = target[len(word):]
                suffix_ways = all_construct(suffix, word_bank, memo)
                target_ways = [[word] + ways for ways in suffix_ways]

                for ways in target_ways:
                    result.append(ways)

        except ValueError:
            continue

    memo[target] = result
    return result


print(all_construct(target_1, sub_strings_1, {}))
print(all_construct(target_2, sub_strings_2, {}))
print(all_construct(target_3, sub_strings_3, {}))
print(all_construct(target_4, sub_strings_4, {}))
