def least_interval(tasks: list[str], n: int) -> int:
    if n == 0:
        return len(tasks)

    freqs = [0] * 26

    for task in tasks:
        freqs[ord(task) - 65] += 1

    freqs.sort()
    f_max = freqs.pop()
    num_gaps = f_max - 1
    idle_time = num_gaps * n

    while freqs and idle_time > 0:
        idle_time -= min(num_gaps, freqs.pop())

    idle_time = max(0, idle_time)

    return idle_time + len(tasks)


tasks_1 = ["A", "A", "A", "B", "B", "B"]
n_1 = 2

print(least_interval(tasks_1, n_1))

tasks_2 = ["A", "A", "A", "B", "B", "B"]
n_2 = 0

print(least_interval(tasks_2, n_2))

tasks_3 = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n_3 = 2

print(least_interval(tasks_3, n_3))

tasks_4 = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
n_4 = 2

print(least_interval(tasks_4, n_4))
