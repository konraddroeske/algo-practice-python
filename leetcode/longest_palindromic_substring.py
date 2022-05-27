s_1 = "babad"
s_2 = "cbbd"


def longest_palindrome_brute_force(s: str) -> str:
    palindomes = []

    for i, outer in enumerate(s):
        current = outer
        for _, inner in enumerate(s[i + 1:]):
            current += inner

            if current == current[::-1]:
                palindomes.append(current)

    return max(palindomes, key=len)


print(longest_palindrome_brute_force(s_1))
print(longest_palindrome_brute_force(s_2))


# def longest_palindrome_dp(s: str) -> str:
