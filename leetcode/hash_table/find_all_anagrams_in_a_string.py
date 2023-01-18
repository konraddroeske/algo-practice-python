from collections import defaultdict, Counter


def find_anagrams(s: str, p: str) -> list[int]:
    if len(s) < len(p):
        return []

    result = []
    p_count = Counter(p)
    s_count = Counter()

    left = 0
    right = 0

    while right <= len(s):
        if right - left < len(p):
            s_count[s[right]] += 1
            right += 1
            continue

        if p_count == s_count:
            result.append(left)

        s_count[s[left]] -= 1

        if right < len(s):
            s_count[s[right]] += 1

        # move
        left += 1
        right += 1

    return result


print(find_anagrams("cbaebabacd", "abc"))
print(find_anagrams("abab", "ab"))
print(find_anagrams("baa", "aa"))
print(find_anagrams("aaaaaaaaaa", "aaaaaaaaaaaaa"))
