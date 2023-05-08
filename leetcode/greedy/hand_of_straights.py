import heapq
from collections import Counter


# Time - O(n log n)
def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size != 0:
        return False

    cards = Counter(hand)
    min_heap = list(cards.keys())
    heapq.heapify(min_heap)

    while min_heap:
        card = min_heap[0]

        for i in range(card, card + group_size):
            if i not in cards:
                return False

            cards[i] -= 1

            if cards[i] == 0:
                if i != min_heap[0]:
                    return False

                heapq.heappop(min_heap)

    return True


hand_1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
group_size_1 = 3
# true

print(is_n_straight_hand(hand_1, group_size_1))

hand_2 = [1, 2, 3, 4, 5]
group_size_2 = 4
# false

print(is_n_straight_hand(hand_2, group_size_2))

hand_3 = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
group_size_3 = 3
# true

print(is_n_straight_hand(hand_3, group_size_3))

hand_4 = [1, 1, 2, 2, 3, 3]
group_size_4 = 2
# false

print(is_n_straight_hand(hand_4, group_size_4))
