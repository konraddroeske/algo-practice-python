numeral_to_int = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

special_cases = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}

s_1 = "III"
s_2 = "LVIII"
s_3 = "MCMXCIV"
s_4 = "MMMXLV"


# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.


def roman_to_int(s: str) -> int:
    # split into array
    # iterate through characters, check special rules, and add to overall counter
    values: list[tuple[str, int]] = []

    chars = list(s)

    # print(chars)

    for index, char in enumerate(chars):
        # print('values', values)
        if values and (values[-1][0] + char) in special_cases:
            new_key = values[-1][0] + char
            values[-1] = (new_key, special_cases[new_key])
        else:
            values.append((char, numeral_to_int[char]))

    # print(values)

    return sum([val[1] for val in values])


print(roman_to_int(s_1))
print(roman_to_int(s_2))
print(roman_to_int(s_3))
print(roman_to_int(s_4))


def roman_to_int_right_pass(s: str) -> int:
    # Auto add the last character to total
    total = numeral_to_int[s[-1]]

    for i in reversed(range(len(s) - 1)):
        cur_val = numeral_to_int[s[i]]
        prev_val = numeral_to_int[s[i + 1]]

        if cur_val < prev_val:
            total -= numeral_to_int[s[i]]
        else:
            total += numeral_to_int[s[i]]

    return total


print(roman_to_int_right_pass(s_1))
print(roman_to_int_right_pass(s_2))
print(roman_to_int_right_pass(s_3))
print(roman_to_int_right_pass(s_4))
