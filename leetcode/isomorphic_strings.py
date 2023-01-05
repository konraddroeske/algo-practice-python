from typing import Optional

# def check_match(hash_map) -> bool:


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_map: dict[str, Optional[str]] = {}
    t_map: dict[str, Optional[str]] = {}

    for index in range(len(s)):
        s_char = s[index]
        t_char = t[index]

        # check if hash map is empty
        if s_map.get(s_char) is None:
            s_map[s_char] = t_char

        if t_map.get(t_char) is None:
            t_map[t_char] = s_char

        # check if character matches expected character
        if t_char != s_map[s_char] or s_char != t_map[t_char]:
            return False

    return True


s_1 = "egg"
t_1 = "add"

s_2 = "foo"
t_2 = "bar"

s_3 = "paper"
t_3 = "title"

s_4 = "badc"
t_4 = "baba"

print(is_isomorphic(s_1, t_1))
print(is_isomorphic(s_2, t_2))
print(is_isomorphic(s_3, t_3))
print(is_isomorphic(s_4, t_4))
