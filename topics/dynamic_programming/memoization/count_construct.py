target_1 = "abcdef"
sub_strings_1 = ["ab", "abc", "cd", "def", "abcd"]

target_2 = "skateboard"
sub_strings_2 = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]

target_3 = "enterapotentpot"
sub_strings_3 = ["a", "p", "ent", "enter", "ot", "o", "t"]


# m = target string length
# n = word bank length

def count_construct(
        target: str,
        word_bank: list[str],
        memo: dict[str, int],
) -> int:
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    total_count = 0

    for word in word_bank:
        try:
            index = target.index(word)

            if index == 0:
                suffix = target[len(word):]

                num_ways = count_construct(suffix, word_bank, memo)
                total_count += num_ways

        except ValueError:
            continue

    memo[target] = total_count
    return total_count


print(count_construct(target_1, sub_strings_1, {}))
print(count_construct(target_2, sub_strings_2, {}))
print(count_construct(target_3, sub_strings_3, {}))
