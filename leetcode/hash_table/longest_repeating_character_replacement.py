from collections import Counter, defaultdict


def character_replacement(s: str, k: int) -> int:
    # return length of longest substring with max k changes
    # raise NotImplementedError
    result = 0
    left_index = 0
    char_counter = Counter()
    most_common = 0

    for right_index, right_char in enumerate(s):
        char_counter[right_char] += 1
        substring_length = (right_index + 1) - left_index
        most_common = max(most_common, char_counter[right_char])

        if substring_length - most_common > k:
            char_counter[s[left_index]] -= 1
            left_index += 1
        else:
            result = max(substring_length, result)

    return result


print(character_replacement("ABAB", 2))
print(character_replacement("AABABBA", 1))
print(character_replacement("AAAA", 2))
print(character_replacement("ABCDE", 1))
print(character_replacement("ABAA", 0))
