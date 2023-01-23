from heapq import heappush, heappop


def last_stone_weight(stones: list[int]) -> int:
    max_heap = []

    for stone in stones:
        heappush(max_heap, -stone)

    while len(max_heap) > 1:
        stone_1 = heappop(max_heap)
        stone_2 = heappop(max_heap)

        if stone_1 == stone_2:
            continue
        else:
            new_stone = abs(stone_1 - stone_2)
            heappush(max_heap, -new_stone)

    if len(max_heap) > 0:
        return abs(heappop(max_heap))

    return 0


print(last_stone_weight([2, 7, 4, 1, 8, 1]))
print(last_stone_weight([1]))
