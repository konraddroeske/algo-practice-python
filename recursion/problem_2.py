# generate all variations of zeroes and ones of some length N
# Input
# N =3
#
# Output
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111


def product_for_loop(chars, repeat):
    array = [tuple(chars)] * repeat
    results = [[]]

    for chars_tuple in array:
        temp = []
        for res in results:
            for c in chars_tuple:
                temp.append(res + [c])

        results = temp

    return results


def product_comprehension(chars, repeat):
    array = [tuple(chars)] * repeat
    results = [[]]

    for chars_tuple in array:
        results = [res + [c] for res in results for c in chars_tuple]

    return results


def product_recursive(arr):
    if not arr:
        return [[]]

    return [res + [c] for c in arr[0]
            for res in product_recursive(arr[1:])]


def problem_2(n: int) -> None:
    chars = '01'
    array = [tuple(chars)] * n
    results = product_recursive(array)

    print(results)


print(problem_2(2))
