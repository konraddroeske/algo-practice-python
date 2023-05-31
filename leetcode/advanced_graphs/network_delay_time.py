import heapq
from collections import defaultdict
from typing import Optional


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    # create adjacency list
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]

    for time in times:
        graph[time[0]].append((time[1], time[2]))

    # distances at inf
    distances: list[float | int] = [float("inf") for _ in range(n + 1)]
    distances[k] = 0

    # priority queue by shortest distance
    # greedy
    min_heap: list[tuple[int, int]] = [(0, k)]
    heapq.heapify(min_heap)

    while min_heap:
        cur_cost, cur_node = heapq.heappop(min_heap)

        if cur_cost > distances[cur_node]:
            continue

        for next_node, next_cost in graph[cur_node]:
            new_cost = cur_cost + next_cost

            if new_cost < distances[next_node]:
                distances[next_node] = new_cost
                heapq.heappush(min_heap, (new_cost, next_node))

    if any(cost == float("inf") for cost in distances[1:]):
        return -1

    return int(max(distances[1:]))


times_1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n_1 = 4
k_1 = 2

result_1 = network_delay_time(times_1, n_1, k_1)
print(result_1)

times_2 = [[1, 2, 1]]
n_2 = 2
k_2 = 1

result_2 = network_delay_time(times_2, n_2, k_2)
print(result_2)

times_3 = [[1, 2, 1]]
n_3 = 2
k_3 = 2

result_3 = network_delay_time(times_3, n_3, k_3)
print(result_3)
