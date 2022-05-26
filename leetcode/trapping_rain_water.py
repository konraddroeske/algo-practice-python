height_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height_2 = [4, 2, 0, 3, 2, 5]


def find_amount_of_water(cur_height: int, max_left: int, max_right: int) -> int:
    amount = min(max_left, max_right) - cur_height

    return amount if amount > 0 else 0


# Solution 1
def trap(height: list[int]) -> int:
    # for each element of array, find the amount of water it can hold
    # min of largest element left / largest element right - cur height
    count = 0
    max_left_height = height[0]

    max_right_pos = 0
    max_right_height = height[max_right_pos]

    for index, cur_height in enumerate(height):
        if index != 0 and index != len(height) - 1:
            if cur_height > max_left_height:
                max_left_height = cur_height

            if index >= max_right_pos:
                right_height = height[index + 1:]
                max_right_pos = index + right_height.index(max(right_height)) + 1
                max_right_height = height[max_right_pos]

            count += find_amount_of_water(cur_height, max_left_height, max_right_height)

    return count


def trap_2(height: list[int]) -> int:
    if not height or len(height) < 3:
        return 0

    volume = 0

    left = 0
    right = len(height) - 1

    l_max = height[left]
    r_max = height[right]

    while left < right:
        l_max = max(height[left], l_max)
        r_max = max(height[right], r_max)

        if l_max <= r_max:
            volume += l_max - height[left]
            left += 1
        else:
            volume += r_max - height[right]
            right -= 1

    return volume


print(trap_2(height_1))
print(trap_2(height_2))
