from collections import defaultdict
from dataclasses import dataclass


# Johnson's Algorithm

# 1 x Bellman-Ford
# Rest using Dijkstra's


@dataclass(repr=True)
class Edge:
    tail: int
    head: int
    length: int


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


for vertex in vertices:
    print(vertex)
