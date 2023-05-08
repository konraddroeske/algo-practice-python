from collections import defaultdict


def partition_labels(s: str) -> list[int]:
    last_index = {}

    for index, char in enumerate(s):
        last_index[char] = index

    results = []
    size = 0
    end = 0

    for index, char in enumerate(s):
        size += 1

        end = max(end, last_index[char])

        if index == end:
            results.append(size)
            size = 0

    return results


s_1 = "ababcbacadefegdehijhklij"
print(partition_labels(s_1))

s_2 = "eccbbbbdec"
print(partition_labels(s_2))

s_3 = "caedbdedda"
print(partition_labels(s_3))
