def is_subsequence(s: str, t: str) -> bool:
    s_index = 0
    t_index = 0

    while s_index < len(s) and t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index += 1
            t_index += 1
        else:
            t_index += 1

    return s_index == len(s)


# def is_subsequence(s: str, t: str) -> bool:
#     if len(s) > len(t):
#         return False
#
#     s_index = 0
#
#     for t_char in t:
#         if t_char == s[s_index]:
#             s_index += 1
#
#     return s_index == len(s)


s_1 = "abc"
t_1 = "ahbgdc"


s_2 = "axc"
t_2 = "ahbgdc"

print(is_subsequence(s_1, t_1))
print(is_subsequence(s_2, t_2))
