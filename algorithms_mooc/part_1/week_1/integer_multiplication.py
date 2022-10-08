# Grade School Algorithm
from functools import reduce
from math import floor
from operator import mul


def grade_school_add(nums: list[int]) -> int:
    return sum(nums)


def grade_school_prod(nums: list[int]) -> int:
    return reduce(mul, nums)


# Karatsuba Multiplication
def karatsuba(num_1: int, num_2: int) -> int:
    num_1_str = str(num_1)
    num_1_mid = floor(len(num_1_str) / 2)

    num_2_str = str(num_2)
    num_2_mid = floor(len(num_2_str) / 2)

    n = len(num_1_str) if len(num_1_str) % 2 == 0 else len(num_1_str) + 1

    if n <= 4:
        return grade_school_prod([num_1, num_2])

    a = num_1_str[:num_1_mid]
    b = num_1_str[num_1_mid:]

    c = num_2_str[:num_2_mid]
    d = num_2_str[num_2_mid:]

    ac = karatsuba(int(a), int(c))
    bd = karatsuba(int(b), int(d))
    ad = karatsuba(int(a), int(d))
    bc = karatsuba(int(b), int(c))

    adbc = grade_school_add([ad, bc])

    result = grade_school_add([(10**n) * ac, (10 ** (n // 2)) * adbc, bd])

    return result


# print(karatsuba(5678, 1234))
# print(5678 * 1234)
# print("")
# print(karatsuba(234, 857))
# print(234 * 857)
# print("")
# print(len(str(3141592653589793238462643383279502884197169399375105820974944592)))

num_1 = 3141592653589793238462643383279502884197169399375105820974944592
num_2 = 2718281828459045235360287471352662497757247093699959574966967627

result_1 = karatsuba(
    num_1,
    num_2,
)

result_2 = num_1 * num_2

print(result_1)
print(result_2)
