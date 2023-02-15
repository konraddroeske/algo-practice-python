import math
from dataclasses import dataclass
from typing import Optional

from tqdm import tqdm


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
        self.edges = []

        self.vertex_reweighted: Optional[int] = None

    def __repr__(self) -> str:
        return f"Vertex(val={self.val}, edges={self.edges})"

    def add(self, edge: Edge) -> None:
        self.edges.append(edge)


input_vertices = []
input_edges = []

with open("./graph_1.txt") as f:
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
            input_vertices[tail - 1].add(new_edge)


source = Vertex(0)

for vertex in input_vertices:
    from_source = Edge(tail=0, head=vertex.val, length=0)
    source.edges.append(from_source)
    input_edges.append(from_source)

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

            # Optimize!
            other_paths = [
                (edge.length + arr[edge.tail][edge_index - 1])
                for edge in all_edges
                if edge.head == cur_vertex.val
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


def dijkstras_shortest_paths(
    cur_source: Vertex, all_vertices: list[Vertex], all_edges: list[Edge]
) -> list[int]:
    processed = {cur_source.val: cur_source}
    shortest_paths = {cur_source.val: 0}

    while len(processed) != len(all_vertices):
        # get all processed edges
        processed_edges: list[Edge] = []

        for processed_vertex in processed.values():
            processed_edges += processed_vertex.edges

        # get edges without head in processed
        outside_edges = [edge for edge in processed_edges if edge.head not in processed]

        edges_with_new_distance: list[tuple[Edge, int]] = []

        # calculate new distance for outside edges
        for outside_edge in outside_edges:
            new_distance = (
                shortest_paths[outside_edge.tail] + outside_edge.length_reweighted
            )
            edges_with_new_distance.append((outside_edge, new_distance))

        if not edges_with_new_distance:
            break

        # get minimum distance
        min_edge, min_distance = min(edges_with_new_distance, key=lambda x: x[1])
        # add vertex to processed
        processed[min_edge.head] = all_vertices[min_edge.head - 1]
        # add min distance to shortest paths
        shortest_paths[min_edge.head] = min_distance

    # convert to original distance
    final_distances = []

    for vertex_val, distance in shortest_paths.items():
        final_distance = (
            distance
            - source.vertex_reweighted
            + all_vertices[vertex_val - 1].vertex_reweighted
        )
        final_distances.append(final_distance)

    return final_distances


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
    paths = []

    for cur_vertex in tqdm(reweighted_vertices):
        paths += dijkstras_shortest_paths(
            cur_vertex, reweighted_vertices, reweighted_edges
        )

    return min(paths)


print(get_shortest_shortest_path(input_vertices, input_edges))
