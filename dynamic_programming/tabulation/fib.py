# 0th number is 0
# 1st number is 1

def fib(n: int) -> int:
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(n):
        if i + 1 < len(table):
            table[i + 1] += table[i]

        if i + 2 < len(table):
            table[i + 2] += table[i]

    return table[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
