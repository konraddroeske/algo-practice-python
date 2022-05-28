s_1 = "babad"
s_2 = "cbbd"
s_3 = "ac"


def longest_palindrome_brute_force(s: str) -> str:
    palindomes = []

    for i, outer in enumerate(s):
        current = outer
        for _, inner in enumerate(s[i + 1:]):
            current += inner

            if current == current[::-1]:
                palindomes.append(current)

    return max(palindomes, key=len)


# print(longest_palindrome_brute_force(s_1))
# print(longest_palindrome_brute_force(s_2))


def longest_palindrome(s: str) -> str:
    longest = ""

    for index, char in enumerate(s):
        longest = max(helper(index, index, s), longest, key=len)

        if index + 1 < len(s):
            longest = max(helper(index, index + 1, s), longest, key=len)

    return longest


def helper(left: int, right: int, s: str) -> str:
    l = left
    r = right

    if s[l] != s[r]:
        return ""

    cur = ""

    while l >= 0 and r < len(s) and s[l] == s[r]:
        new = s[l:r + 1]

        if len(new) > len(cur):
            cur = new

        l -= 1
        r += 1

    return cur


def longest_palindrome_dp(s: str) -> str:
    if len(s) <= 1:
        return s

    table = [[False] * len(s) for _ in range(len(s))]
    longest = s[0]

    for i in range(len(s)):
        table[i][i] = True

    for col in reversed(range(len(s))):
        for row in range(col + 1, len(s)):
            if s[col] == s[row]:
                if row - col == 1 or table[row - 1][col + 1]:
                    table[row][col] = True

                    if (row + 1) - col > len(longest):
                        longest = s[col:row + 1]

    return longest


print(longest_palindrome_dp(s_1))
print(longest_palindrome_dp(s_2))
print(longest_palindrome_dp(s_3))
