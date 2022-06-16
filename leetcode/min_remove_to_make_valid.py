s_1 = "lee(t(c)o)de)"
s_2 = "a)b(c)d"
s_3 = "))(("

# Time - O(n)
# Memory = O(2n) -> O(n)


def min_remove(s: str) -> str:
    result = list(s)  # Time: O(n)
    stack = []

    for index, char in enumerate(result):  # Time: O(n)
        if char == "(":
            stack.append(index)

        if char == ")":
            if stack and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(index)

    while stack:  # Time: O(n)
        index = stack.pop()
        result[index] = ""

    return "".join(result)


print(min_remove(s_1))
print(min_remove(s_2))
print(min_remove(s_3))
