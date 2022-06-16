s_1 = "3+2*2"
s_2 = " 3/2 "
s_3 = " 3+5 / 2 "
s_4 = "0-2147483647"
s_5 = "14-3/2"


# Evaluate math without using Eval
# Ensure expression follows DMAS

def evaluate(num: int, sign: str, stack: list[int]) -> None:
    if sign == "+":
        stack.append(num)
    elif sign == "-":
        stack.append(-num)
    elif sign == "*":
        new_num = stack.pop() * num
        stack.append(new_num)
    else:
        prev_num = stack.pop()

        if prev_num > 0:
            new_num = prev_num // num
        else:
            new_num = -(-1 * prev_num // num)

        stack.append(new_num)


def basic_calculator_2(s: str) -> int:
    stack = []

    operators = ('/', '*', '+', '-')
    prev_num = ""
    prev_sign = "+"

    for char in s:
        if char.isdigit():
            prev_num += char
        elif char in operators:
            evaluate(int(prev_num), prev_sign, stack)
            prev_num = ""
            prev_sign = char

    evaluate(int(prev_num), prev_sign, stack)

    return sum(stack)


print(basic_calculator_2(s_1))
print(basic_calculator_2(s_2))
print(basic_calculator_2(s_3))
print(basic_calculator_2(s_4))
print(basic_calculator_2(s_5))
