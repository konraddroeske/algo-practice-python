from collections import Counter
from heapq import heapify, heappush, heappop


def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    counter = Counter(words)

    max_heap = []

    for key, value in counter.items():
        heappush(max_heap, (-value, key))

    result = []

    for index in range(k):
        result.append(heappop(max_heap)[1])

    return result


print(top_k_frequent_words(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(
    top_k_frequent_words(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    )
)
