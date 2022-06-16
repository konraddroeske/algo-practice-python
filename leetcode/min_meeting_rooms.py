import heapq

intervals_1 = [[0, 30], [5, 10], [15, 20]]
intervals_2 = [[7, 10], [2, 4]]
intervals_3 = [[13, 15], [1, 13]]
intervals_4 = [[13, 15], [1, 13]]


def min_meeting_rooms_bf(intervals: list[list[int]]) -> int:
    max_val = 0

    for interval in intervals:
        for val in interval:
            if val > max_val:
                max_val = val

    table = [0] * (max_val + 1)

    for interval in intervals:
        for minute in range(interval[0], interval[1]):
            table[minute] += 1

    return max(table)


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    events = []

    for interval in intervals:
        events.append((interval[0], 1))
        events.append((interval[1], -1))

    sorted_events = sorted(events, key=lambda x: (x[0], x[1]))

    max_meeting_rooms = 0
    cur_meeting_rooms = 0

    for index, event in enumerate(sorted_events):
        cur_meeting_rooms += event[1]
        max_meeting_rooms = max(max_meeting_rooms, cur_meeting_rooms)

    return max_meeting_rooms


def min_meeting_rooms_min_heap(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[0])  # Time: O(n log n)
    heap = []

    for interval in intervals:
        # is the new start time after or equal to the smallest end time
        # if so, pop and add the new end time
        if heap and interval[0] >= heap[0]:
            heapq.heapreplace(heap, interval[1])
        # else, add the new end time
        else:
            heapq.heappush(heap, interval[1])  # Time: O(n) - worst case, all meetings
            # collide

    return len(heap)


print(min_meeting_rooms_min_heap(intervals_1))
print(min_meeting_rooms_min_heap(intervals_2))
print(min_meeting_rooms_min_heap(intervals_3))
print(min_meeting_rooms_min_heap(intervals_4))
