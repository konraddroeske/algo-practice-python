def get_factorial(n: int) -> int:
    val = 1

    for i in range(n):
        val = val * (i + 1)

    return val


print(get_factorial(5))


def get_factorial_recursion(n: int) -> int:
    if n == 1:
        return 1

    return n * get_factorial_recursion(n - 1)


print(get_factorial_recursion(5))
