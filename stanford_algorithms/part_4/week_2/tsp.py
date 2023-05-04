"""
Traveling salesman problem
"""

import numpy as np
from itertools import combinations

f = open("tsp.txt", "r")
ls = f.readlines()[1:]
full_graph = [list(map(float, i.split(" "))) for i in ls]
graph_1 = full_graph[:13]
graph_2 = full_graph[11:]

print("graph_1", graph_1)
print("graph_2", graph_2)


def dis(i, j, cur_graph):
    return np.sqrt(
        (cur_graph[i][0] - cur_graph[j][0]) ** 2
        + (cur_graph[i][1] - cur_graph[j][1]) ** 2
    )


print("distance", dis(11, 12, full_graph))


def tsp(graph):
    N = len(graph)
    dic1 = {frozenset([0]): {0: 0}}

    for m in range(1, N):
        comb = list(combinations(range(1, N), m))
        dic2 = {
            frozenset(comb[i]): {list(comb[i])[j]: 0 for j in range(m)}
            for i in range(len(comb))
        }
        print(m, len(dic2))
        for s in dic2:
            for j in s:
                ans = []
                if m == 1:
                    dic2[s][j] = dis(0, j, graph)
                else:
                    sj = set(s)
                    sj.remove(j)
                    dic2[s][j] = min(
                        [
                            dic1[frozenset(sj)][k] + dis(k, j, graph)
                            for k in sj
                            if k != j
                        ]
                    )
        dic1 = dic2.copy()
    return min(
        [dic1[frozenset(range(1, N))][k] + dis(k, 0, graph) for k in range(1, N)]
    )


# print(tsp)
result_1 = tsp(graph_1)
result_2 = tsp(graph_2)
distance = dis(11, 12, full_graph)

print(result_1)
print(result_2)
print(distance)

print(result_1 + result_2 - (distance * 2))
