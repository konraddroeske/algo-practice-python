# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


def climb_stairs(n: int) -> int:
    result = [1, 1]

    for step in range(2, n + 1):
        result.append(result[step - 1] + result[step - 2])

    return result[-1]


print(climb_stairs(5))
