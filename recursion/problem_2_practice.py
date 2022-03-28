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

def product_fot_loop(arr: list[tuple[str]]) -> None:
    results = [[]]

    for char_tuple in arr:
        temp = []

        for res in results:
            for c in char_tuple:
                temp.append(res + [c])

        results = temp

    print(results)


def product_list_comprehension(arr: list[tuple[str]]) -> None:
    results = [[]]

    for chars_tuple in arr:
        results = [res + [c] for res in results for c in chars_tuple]

    print(results)


def product_recursive(arr: list[tuple[str]]) -> list[list[str]]:
    if not arr:
        return [[]]

    return [res + [c] for c in arr[0] for res in product_recursive(arr[1:])]


def generate_pattern(chars: str, n: int):
    arr = [tuple(chars)] * n

    # pattern_for_loop(arr)
    # pattern_comprehension(arr)

    results = product_recursive(arr)
    print('recursive', results)


generate_pattern('01', 3)
