strs_1 = ["flower", "flow", "flight"]
strs_2 = ["dog", "racecar", "car"]
strs_3 = ["dog", "dogs", "doggy"]


def longest_common_prefix(strs: list[str]) -> str:
    shortest = len(min(strs, key=len))
    result = ""

    for index in range(shortest):
        chars = set()

        for word in strs:
            chars.add(word[index])

        if len(chars) == 1:
            result += chars.pop()
        else:
            break

    return result


print(longest_common_prefix(strs_1))
print(longest_common_prefix(strs_2))
print(longest_common_prefix(strs_3))


def longest_common_prefix_2(strs: list[str]) -> str:
    if not strs:
        return ""

    shortest = min(strs, key=len)

    for index, char in enumerate(shortest):
        for other in strs:
            if char != other[index]:
                return other[:index]

    return shortest


print(longest_common_prefix_2(strs_1))
print(longest_common_prefix_2(strs_2))
print(longest_common_prefix_2(strs_3))
