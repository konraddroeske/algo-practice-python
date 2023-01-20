def isBadVersion(version: int) -> bool:
    return version >= 2


def first_bad_version(n: int) -> int:
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


print(first_bad_version(5))
