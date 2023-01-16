def fib(n: int) -> int:
    hash_table = {0: 0, 1: 1}

    for index in range(2, n + 1):
        hash_table[index] = hash_table[index - 1] + hash_table[index - 2]

    return hash_table[n]


print(fib(3))
