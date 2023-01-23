def decode_string(s: str) -> str:
    cur_str = ""
    cur_num = ""
    stack = []

    for char in s:
        if char == "[":
            stack.append(int(cur_num))
            stack.append(cur_str)
            cur_num = ""
            cur_str = ""
        elif char == "]":
            prev_str = stack.pop()
            prev_num = stack.pop()
            cur_str = prev_str + prev_num * cur_str
        elif char.isnumeric():
            cur_num += char
        else:
            cur_str += char

    return cur_str


print(decode_string("3[a]2[bc]"))  # "aaabcbc"
print(decode_string("3[a2[c2[e]]]ef"))  # "accaccacc"
print(decode_string("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
