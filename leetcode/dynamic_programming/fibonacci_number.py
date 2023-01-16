def fib(n: int) -> int:
    hash_table = {0: 0, 1: 1}

    for index in range(2, n + 1):
        hash_table[index] = hash_table[index - 1] + hash_table[index - 2]

    return hash_table[n]

def fib_arr(n: int) -> int:
    arr = [0, 1]

    for index in range(2, n + 1):
        arr.append(arr[index - 1] + arr[index - 2])

    return arr[n]


print(fib(4))
print(fib_arr(4))
