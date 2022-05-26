s_1 = "()"
s_2 = "()[]{}"
s_3 = "([])(){[]}"
s_4 = "([)]"


def valid_parentheses(s: str) -> bool:
    matching = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    stack = []

    try:
        for p in s:
            # if top of stack matches closing bracket, pop off
            # else, add to stack
            if stack and matching[stack[-1]] == p:
                stack.pop()
            else:
                stack.append(p)
    except (KeyError, IndexError):
        return False

    return not stack


print(valid_parentheses(s_1))
print(valid_parentheses(s_2))
print(valid_parentheses(s_3))
print(valid_parentheses(s_4))


def valid_parentheses_2(s: str) -> bool:
    stack = []
    matching = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching.keys():
            if not stack or matching[char] != stack.pop():
                return False
        else:
            return False

    return not stack


print(valid_parentheses_2(s_1))
print(valid_parentheses_2(s_2))
print(valid_parentheses_2(s_3))
print(valid_parentheses_2(s_4))
