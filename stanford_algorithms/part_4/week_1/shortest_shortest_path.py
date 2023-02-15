import math
import multiprocessing
from dataclasses import dataclass
from functools import partial
from typing import Optional

from tqdm import tqdm
from tqdm.contrib.concurrent import process_map


@dataclass
class Edge:
    tail: int
    head: int
    length: int

    tail_reweighted: Optional[int] = None
    head_reweighted: Optional[int] = None

    @property
    def length_reweighted(self) -> Optional[int]:
        if self.tail_reweighted is not None and self.head_reweighted is not None:
            return self.length + self.tail_reweighted - self.head_reweighted

        return None

    def __repr__(self) -> str:
        return (
            f"Edge(tail: {self.tail}, head: {self.head}, tail_reweighted: "
            f"{self.tail_reweighted}, head_reweighted: "
            f"{self.head_reweighted}, length_reweighted: "
            f"{self.length_reweighted})"
        )


class Vertex:
    def __init__(self, val: int) -> None:
        self.val = val
        self.out_edges = []
        self.in_edges = []

        self.vertex_reweighted: Optional[int] = None
        self.distances: list[int] = []

    def __repr__(self) -> str:
        return (
            f"Vertex(val={self.val}, out_edges={self.out_edges}, "
            f"in_edges={self.in_edges})"
        )

    def add_out_edge(self, edge: Edge) -> None:
        self.out_edges.append(edge)

    def add_in_edge(self, edge: Edge) -> None:
        self.in_edges.append(edge)


input_vertices = []
input_edges = []

with open("./graph_3.txt") as f:
    for index, line in enumerate(f):
        values = tuple(int(val) for val in str.split(line))

        if index == 0:
            num_vertices, num_edges = values

            for v_index in range(1, num_vertices + 1):
                input_vertices.append(Vertex(v_index))

        else:
            tail, head, length = values
            new_edge = Edge(tail, head, length)
            input_edges.append(new_edge)
            input_vertices[tail - 1].add_out_edge(new_edge)
            input_vertices[head - 1].add_in_edge(new_edge)


# print(input_vertices)

source = Vertex(0)

for vertex in input_vertices:
    edge_from_source = Edge(tail=0, head=vertex.val, length=0)
    source.add_out_edge(edge_from_source)
    input_vertices[edge_from_source.head - 1].add_in_edge(edge_from_source)
    input_edges.append(edge_from_source)


input_vertices = [source] + input_vertices

# Bellman-Ford
def bellman_ford(
    all_vertices: list[Vertex], all_edges: list[Edge]
) -> Optional[tuple[list[Vertex], list[Edge]]]:
    n = len(all_vertices)

    # add extra edge to check for negative cycle
    arr: list[list[Optional[float]]] = [
        [None for _edges in range(n + 1)] for _vertices in range(n)
    ]

    # base case
    for vertex_index in range(len(arr)):
        if vertex_index == 0:
            arr[vertex_index][0] = 0
        else:
            arr[vertex_index][0] = math.inf

    for edge_index in tqdm(range(1, n + 1)):
        for vertex_index, cur_vertex in enumerate(all_vertices):
            case_1 = arr[vertex_index][edge_index - 1]

            other_paths = [
                (edge.length + arr[edge.tail][edge_index - 1])
                for edge in cur_vertex.in_edges
            ]

            case_2 = min(other_paths) if other_paths else 0

            arr[vertex_index][edge_index] = min(case_1, case_2)

    # check for negative cycle
    for vertex_index, cur_vertex in enumerate(all_vertices):
        last_edge_weight = arr[vertex_index][n - 1]
        extra_edge_weight = arr[vertex_index][n]

        if last_edge_weight != extra_edge_weight:
            return None

        cur_vertex.vertex_reweighted = extra_edge_weight

    for edge in all_edges:
        edge.tail_reweighted = all_vertices[edge.tail].vertex_reweighted
        edge.head_reweighted = all_vertices[edge.head].vertex_reweighted

    # remove source
    final_vertices = [v for v in all_vertices if v.val != 0]
    final_edges = [e for e in all_edges if e.tail != 0]

    return final_vertices, final_edges


def dijkstras_shortest_path(all_vertices: list[Vertex], cur_source: Vertex) -> int:
    processed = {cur_source.val: cur_source}
    outside_edges = [edge for edge in cur_source.out_edges]
    shortest_paths = {cur_source.val: 0}

    while len(processed) != len(all_vertices) and outside_edges:
        min_outside_edge: Optional[tuple[Edge, int]] = None

        # get min outside edge
        for outside_edge in outside_edges:
            new_distance = (
                shortest_paths[outside_edge.tail] + outside_edge.length_reweighted
            )
            cur_edge = (outside_edge, new_distance)

            if min_outside_edge is None:
                min_outside_edge = cur_edge
            else:
                min_outside_edge = min(min_outside_edge, cur_edge, key=lambda x: x[1])

        if min_outside_edge is None:
            break

        # get minimum distance
        min_edge, min_distance = min_outside_edge

        # add vertex to processed
        new_vertex = all_vertices[min_edge.head - 1]
        processed[min_edge.head] = new_vertex

        # remove inside edges
        outside_edges = [edge for edge in outside_edges if edge.head not in processed]

        # add new outside edges
        for edge in new_vertex.out_edges:
            if edge.head not in processed:
                outside_edges.append(edge)

        # add min distance to shortest paths
        shortest_paths[min_edge.head] = min_distance

    # convert to original distance
    final_distances = []

    for vertex_val, distance in shortest_paths.items():
        final_distance = (
            distance
            - cur_source.vertex_reweighted
            + all_vertices[vertex_val - 1].vertex_reweighted
        )

        final_distances.append(final_distance)

    return min(final_distances) if final_distances else 0


def get_shortest_shortest_path(
    vertices: list[Vertex], edges: list[Edge]
) -> Optional[int]:
    result = bellman_ford(vertices, edges)

    if result is None:
        print("Negative cycle.")
        return None

    print("Not a negative cycle, using Dijkstra's...")
    reweighted_vertices, reweighted_edges = result

    # Dijkstra's
    dijkstras_partial = partial(dijkstras_shortest_path, reweighted_vertices)

    all_paths = process_map(dijkstras_partial, reweighted_vertices)

    return min(all_paths)


print(get_shortest_shortest_path(input_vertices, input_edges))
