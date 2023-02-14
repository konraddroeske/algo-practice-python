import itertools
import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional


# Johnson's Algorithm

# 1 x Bellman-Ford
# Rest using Dijkstra's


@dataclass(repr=True)
class Edge:
    tail: int
    head: int
    length: int
    tail_reweighted: Optional[int] = None
    head_reweighted: Optional[int] = None

    @property
    def length_reweighted(self) -> Optional[int]:
        if self.tail_reweighted and self.head_reweighted:
            return self.length + self.tail_reweighted - self.head_reweighted

        return None


class Vertex:
    def __init__(self, val: int) -> None:
        self.val = val
        self.edges = []

    def __repr__(self) -> str:
        return f"Vertex(val={self.val}, edges={self.edges})"

    def add(self, edge: Edge) -> None:
        self.edges.append(edge)


vertices = []
edges = []

with open("./test_graph.txt") as f:
    for index, line in enumerate(f):
        values = tuple(int(val) for val in str.split(line))

        if index == 0:
            num_vertices, num_edges = values

            for v_index in range(1, num_vertices + 1):
                vertices.append(Vertex(v_index))

        else:
            tail, head, length = values
            new_edge = Edge(tail, head, length)
            edges.append(new_edge)
            vertices[tail - 1].add(new_edge)


source = Vertex(0)

for vertex in vertices:
    from_source = Edge(tail=0, head=vertex.val, length=0)
    source.edges.append(from_source)

vertices = [source] + vertices

# Bellman-Ford
def bellman_ford(all_vertices: list[Vertex]) -> list[Vertex]:
    n = len(all_vertices)

    arr = [[None for _vertices in range(n)] for _edges in range(n - 1)]

    # for num edges = 0, vertex = source
    arr[0][0] = 0

    # for num edges = 0, vertex != source
    for vertex_index in range(len(arr[0])):
        arr[0][vertex_index] = 0

    # print(arr)
    # for row in arr:
    #     print(row)

    for edge_index in range(1, n - 1):
        for vertex_index, v in enumerate(all_vertices):
            case_1 = arr[edge_index - 1][vertex_index]
            # case_2 = min


vertices = bellman_ford(vertices)

# Dijkstra's
