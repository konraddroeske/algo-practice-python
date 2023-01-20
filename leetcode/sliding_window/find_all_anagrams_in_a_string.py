from collections import Counter


def find_anagrams(s: str, p: str) -> list[int]:
    if len(s) < len(p):
        return []

    result = []
    p_count = Counter(p)
    s_count = Counter()

    for right_index, char in enumerate(s):
        s_count[char] += 1

        left_index = right_index - len(p)

        if left_index >= 0:
            s_count[s[left_index]] -= 1

        if s_count == p_count:
            result.append(left_index + 1)

    return result


print(find_anagrams("cbaebabacd", "abc"))
print(find_anagrams("abab", "ab"))
print(find_anagrams("baa", "aa"))
print(find_anagrams("aaaaaaaaaa", "aaaaaaaaaaaaa"))
