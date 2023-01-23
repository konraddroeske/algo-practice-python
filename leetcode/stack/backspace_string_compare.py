def backspace_compare(s: str, t: str) -> bool:
    stack_s = []
    stack_t = []

    for char in s:
        if char != "#":
            stack_s.append(char)
        elif stack_s:
            stack_s.pop()

    for char in t:
        if char != "#":
            stack_t.append(char)
        elif stack_t:
            stack_t.pop()

    return stack_s == stack_t


def backspace_compare_optimized(s: str, t: str) -> bool:
    counter_s = 0
    counter_t = 0
    pointer_s = len(s) - 1
    pointer_t = len(t) - 1

    while pointer_s >= 0 or pointer_t >= 0:
        char_s = s[pointer_s] if pointer_s >= 0 else ""
        char_t = t[pointer_t] if pointer_t >= 0 else ""

        if char_s == "#":
            counter_s += 1
            pointer_s -= 1
        elif char_t == "#":
            counter_t += 1
            pointer_t -= 1
        elif counter_s > 0:
            counter_s -= 1
            pointer_s -= 1
        elif counter_t > 0:
            counter_t -= 1
            pointer_t -= 1
        else:
            if char_s != char_t:
                return False

            pointer_s -= 1
            pointer_t -= 1

    return True


print(backspace_compare_optimized("ab#c", "ad#c"))  # true
print(backspace_compare_optimized("ab##", "c#d#"))  # true
print(backspace_compare_optimized("a#c", "b"))  # false
print(backspace_compare_optimized("y#fo##f", "y#f#o##f"))  # true

print(backspace_compare_optimized("bxj##tw", "bxj###tw"))  # false
print(backspace_compare_optimized("hd#dp#czsp#####", "hd#dp#czsp######"))  # false
