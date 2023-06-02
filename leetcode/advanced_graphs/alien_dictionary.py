from collections import defaultdict
from typing import Optional


def alien_order(words: list[str]) -> str:
    graph = {c: set() for w in words for c in w}

    # Compare strings 2 at a time and build adj list
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_length = min(len(w1), len(w2))

        if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
            return ""

        for j in range(min_length):
            if w1[j] != w2[j]:
                graph[w1[j]].add(w2[j])
                break

    visited = {}
    result = []

    def dfs(c: str) -> bool:
        if c in visited:
            return visited[c]

        visited[c] = True

        for nei in graph[c]:
            if dfs(nei):
                return True

        visited[c] = False
        result.append(c)

    for c in graph:
        if dfs(c):
            return ""

    result.reverse()
    return "".join(result)


# words_1 = ["wrt", "wrf", "er", "ett", "rftt"]
# result_1 = alien_order(words_1)
# print("result 1", result_1)
#
# words_2 = ["z", "x", "z"]
# result_2 = alien_order(words_2)
# print("result 2", result_2)
#
# words_3 = ["z", "x"]
# result_3 = alien_order(words_3)
# print("result 3", result_3)

words_4 = ["zy", "zx"]
result_4 = alien_order(words_4)
print("result 4", result_4)
