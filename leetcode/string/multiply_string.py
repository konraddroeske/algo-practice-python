def multiply(num1: str, num2: str) -> str:
    final = 0

    for index_x in range(len(num2) - 1, -1, -1):
        result = 0
        carry = 0

        for index_y in range(len(num1) - 1, -1, -1):
            multiplied = (int(num2[index_x]) * int(num1[index_y])) + carry
            power_y = (len(num1) - 1) - index_y

            if index_y == 0:
                result += multiplied * (10**power_y)
            else:
                carry, digit = divmod(multiplied, 10)
                result += digit * (10**power_y)

        power_x = (len(num2) - 1) - index_x
        final += result * (10**power_x)

    return str(final)


print(2 * 3)
print(multiply("2", "3"))

print(123 * 456)
print(multiply("123", "456"))

print(12123 * 1982741981)
print(multiply("12123", "1982741981"))
