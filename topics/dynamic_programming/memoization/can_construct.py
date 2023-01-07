target_1 = "abcdef"
sub_strings_1 = ["ab", "abc", "cd", "def", "abcd"]

target_2 = "skateboard"
sub_strings_2 = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]


# height of tree: m
# branching factor: n - words in the word bank

# Brute Force
# time: O(n ^ m * m) - 2nd m from slice target
# space: O(m * m) - height of call stack * string of length m (suffix)

# Dynamic Programming
# time: O(n * m ^ 2)
# space: O(m ^ 2)

def can_construct(
        target: str,
        word_bank: list[str],
        memo: dict[str, bool]) \
        -> bool:
    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in word_bank:
        try:
            index = target.index(word)

            if index == 0:
                suffix = target[len(word):]

                if can_construct(suffix, word_bank, memo) is True:
                    memo[target] = True
                    return True

        except ValueError:
            continue

    memo[target] = True
    return False


print(can_construct(target_1, sub_strings_1, {}))
print(can_construct(target_2, sub_strings_2, {}))
