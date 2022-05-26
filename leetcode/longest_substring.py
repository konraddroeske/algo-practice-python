s_1 = "abcabcbb"
s_2 = "bbbbb"
s_3 = "pwwkew"
s_4 = " "
s_5 = "aab"
s_6 = "dvdf"
s_7 = "bbtablud"
s_8 = "loddktdji"


def longest_substring(s: str) -> int:
    count = 0
    sub_string = ""

    for char in s:
        if char not in sub_string:
            sub_string += char
            count = max(len(sub_string), count)
        else:
            index = sub_string.index(char)
            sub_string = sub_string[index + 1:] + char

    return count


print(longest_substring(s_1))
print(longest_substring(s_2))
print(longest_substring(s_3))
print(longest_substring(s_4))
print(longest_substring(s_5))
print(longest_substring(s_6))
print(longest_substring(s_7))
print(longest_substring(s_8))


def longest_substring_hash(s: str) -> int:
    left = 0
    max_length = 0
    used_chars = {}

    for index, char in enumerate(s):
        if char in used_chars and left <= used_chars[char]:
            left = used_chars[char] + 1
        else:
            max_length = max(max_length, index - left + 1)

        used_chars[char] = index

    return max_length


print(longest_substring_hash(s_1))
print(longest_substring_hash(s_2))
print(longest_substring_hash(s_3))
print(longest_substring_hash(s_4))
print(longest_substring_hash(s_5))
print(longest_substring_hash(s_6))
print(longest_substring_hash(s_7))
print(longest_substring_hash(s_8))
