def happy_number(n: int) -> bool:
    prev_results = set()

    def get_sum_of_digits(num: int) -> int:
        total = 0

        while num > 0:
            num, digit = divmod(num, 10)
            total += digit**2

        return total

    while n > 1 and n not in prev_results:
        prev_results.add(n)
        n = get_sum_of_digits(n)
        print(n)

    return n == 1


# print(happy_number(19))
# print(happy_number(2))
print(happy_number(7))
