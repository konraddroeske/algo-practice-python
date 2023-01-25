def longest_common_prefix(strs: list[str]) -> str:
    cur_char = set()
    result = ""

    for index in range(len(min(strs))):
        for word in strs:
            cur_char.add(word[index])

        if len(cur_char) == 1:
            result += cur_char.pop()
        else:
            break

    return result


def longest_common_prefix_zip(strs: list[str]) -> str:
    result = ""

    for chars_tuple in zip(*strs):
        if len(set(chars_tuple)) == 1:
            result += chars_tuple[0]
        else:
            return result

    return result


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
