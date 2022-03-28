# N=2
# *
# **
# *
#
# N=3
# *
# **
# ***
# **
# *
#
# For inputs of N, draw this pattern.
# But using recursion, without any for/while loops.

def pattern_1(n: int, i: int) -> None:
    if i < n:
        val = '*' * i
        print(val)
        pattern_1(n, i + 1)


def pattern_2(n: int) -> None:
    if n > 0:
        val = '*' * n
        print(val)
        pattern_2(n - 1)


def print_stars(n: int) -> None:
    pattern_1(n, 1)
    pattern_2(n)


print_stars(2)
print_stars(3)
print_stars(4)
