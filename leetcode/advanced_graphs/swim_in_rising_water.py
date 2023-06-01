import heapq
from typing import Optional


# Time - O(e * log v)
def swim_in_water(grid: list[list[int]]) -> int:
    rows = len(grid) - 1
    cols = len(grid[0]) - 1

    visited = set()
    visited.add((0, 0))

    min_heap = [(grid[0][0], 0, 0)]
    directions = [-1, 0], [1, 0], [0, -1], [0, 1]

    heapq.heapify(min_heap)

    while min_heap:
        ct, cr, cc = heapq.heappop(min_heap)

        if cr == rows and cc == cols:
            return ct

        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc

            if nr < 0 or nr > rows or nc < 0 or nc > cols or (nr, nc) in visited:
                continue

            visited.add((nr, nc))
            heapq.heappush(min_heap, (max(ct, grid[nr][nc]), nr, nc))

    raise TypeError("Could not find min time.")


grid_1 = [[0, 2], [1, 3]]
result_1 = swim_in_water(grid_1)
print("result 1", result_1)

grid_2 = [
    [0, 1, 2, 3, 4],
    [24, 23, 22, 21, 5],
    [12, 13, 14, 15, 16],
    [11, 17, 18, 19, 20],
    [10, 9, 8, 7, 6],
]
result_2 = swim_in_water(grid_2)
print("result 2", result_2)
