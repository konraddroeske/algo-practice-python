# write a program, that prints out all possible permutations of an array of length N
# N = 3
#
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
#
#
# Input N = 4
#
# 1 2 3 4
# 1 2 4 3
# ... and so on

def permutation_for_loop(n: int) -> None:
    arr = [list(range(1, n + 1))] * n
    print('arr', arr)

    products = [[]]

    for chars_arr in arr:
        temp = []

        for product in products:
            for c in chars_arr:
                if c not in product:
                    temp.append(product + [c])

        products = temp

    print(products)


def permutation_list_comprehension(n: int) -> None:
    arr = [list(range(1, n + 1))] * n
    products = [[]]

    for chars_arr in arr:
        products = [product + [c] for product in products for c in chars_arr if
                    c not in product]

    print(products)


def permutation_recursive(arr: list[list[int]]) -> list[list[int]]:
    if not arr:
        return [[]]

    return [product + [c] for c in arr[0] for product in
            permutation_recursive(arr[1:]) if c not in product]


def generate_pattern(n: int) -> None:
    permutation_for_loop(n)
    permutation_list_comprehension(n)

    arr = [list(range(1, n + 1))] * n
    results = permutation_recursive(arr)

    for res in results:
        print(res)


generate_pattern(3)
