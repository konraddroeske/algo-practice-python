import heapq


def min_cost_connect_points(points: list[list[int]]) -> int:
    distance = 0

    prev = tuple(points[0])
    visited = {prev}
    remaining = {tuple(point) for point in points[1:]}

    min_heap = []

    while remaining:
        for cur in remaining:
            cur_min = abs(prev[0] - cur[0]) + abs(prev[1] - cur[1])
            heapq.heappush(min_heap, (cur_min, cur))

        while min_heap and min_heap[0][1] in visited:
            heapq.heappop(min_heap)

        if min_heap:
            min_distance, min_point = heapq.heappop(min_heap)
            distance += min_distance
            prev = min_point
            visited.add(min_point)
            remaining.remove(min_point)

    return distance


# O(n^2 log n)
def min_cost_connect_points_prims(points: list[list[int]]) -> int:
    n = len(points)

    adj = {i: [] for i in range(n)}

    for i in range(n):
        x1, y1 = points[i]

        for j in range(i + 1, n):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    res = 0
    visit = set()
    min_heap = [[0, 0]]  # [cost, point]

    while len(visit) < n:
        cost, i = heapq.heappop(min_heap)

        if i in visit:
            continue

        res += cost
        visit.add(i)

        for nei_cost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(min_heap, [nei_cost, nei])

    return res


points_1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
result_1 = min_cost_connect_points_prims(points_1)
print(f"result 1: {result_1}")

points_2 = [[3, 12], [-2, 5], [-4, 1]]
result_2 = min_cost_connect_points_prims(points_2)
print(f"result 2: {result_2}")
