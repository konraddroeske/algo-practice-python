import random
from typing import Optional


class Edge:
    def __init__(self, endpoint_1: int, endpoint_2: int) -> None:
        self.endpoint_1 = endpoint_1
        self.endpoint_2 = endpoint_2

    def __repr__(self) -> str:
        return f"Edge({self.endpoint_1}, {self.endpoint_2})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Edge):
            return (
                self.endpoint_1 == other.endpoint_1
                and self.endpoint_2 == other.endpoint_2
            )

        return False

    def is_self_loop(self) -> bool:
        return self.endpoint_1 == self.endpoint_2


class Vertex:
    def __init__(self, index: int, edges: list[Edge]) -> None:
        self.index = index
        self.edges = edges

    def __repr__(self) -> str:
        return f"Vertex(index: {self.index}, edges: {self.edges})"


def is_edge_duplicate(cur_edge: Edge, all_edges: list[Edge]) -> bool:
    for edge in all_edges:
        if (
            cur_edge.endpoint_1 == edge.endpoint_1
            and cur_edge.endpoint_2 == edge.endpoint_2
        ) or (
            cur_edge.endpoint_1 == edge.endpoint_2
            and cur_edge.endpoint_2 == edge.endpoint_1
        ):
            return True

    return False


def get_edges_and_vertices() -> tuple[list[Edge], list[Vertex]]:
    all_edges: list[Edge] = []
    all_vertices: list[Vertex] = []

    with open("mincut_input.txt") as f:
        for line in f:
            vals = [int(x) for x in str.split(line)]

            vertex_index = vals[0]
            endpoints = vals[1:]

            # Create all edges
            new_edges = [
                new_edge
                for endpoint in endpoints
                if not is_edge_duplicate(
                    (new_edge := Edge(vertex_index, endpoint)), all_edges
                )
            ]

            # Add if edge does not exist
            all_edges += new_edges

            # Create all vertices
            new_vertex = Vertex(vertex_index, new_edges)
            all_vertices.append(new_vertex)

    # print(len(all_vertices))

    # for vertex in all_vertices:
    #     print(vertex.index)

    return all_edges, all_vertices


# random.seed(1)


class Graph:
    def __init__(self, vertices: list[Optional[Vertex]], edges: list[Edge]) -> None:
        self.vertices = vertices
        self.edges = edges

    def get_vertex(self, index: int) -> Vertex:
        vertex = self.vertices[index - 1]

        if vertex is None:
            raise TypeError("Vertex cannot be None: %r", index)

        return vertex

    def pick_random_edge(self) -> Edge:
        return random.choice(self.edges)

    def remove_vertex(self, index: int) -> list[Optional[Vertex]]:
        self.vertices[index - 1] = None
        return self.vertices

    def merge_vertices(self, random_edge: Edge) -> Vertex:
        u = self.get_vertex(random_edge.endpoint_1)
        v = self.get_vertex(random_edge.endpoint_2)

        # Remove input edge from vertices and edges
        u.edges = [edge for edge in u.edges if random_edge != edge]
        v.edges = [edge for edge in v.edges if random_edge != edge]
        self.edges = [edge for edge in self.edges if random_edge != edge]

        # In all edges, replace v index with u index
        for edge in self.edges:
            if edge.endpoint_1 == v.index:
                edge.endpoint_1 = u.index

            if edge.endpoint_2 == v.index:
                edge.endpoint_2 = u.index

        # Add v edges to u edges
        u.edges += v.edges

        # Delete v vertex from vertices
        self.vertices = self.remove_vertex(random_edge.endpoint_2)

        return u

    def remove_self_loops(self, vertex: Vertex) -> list[Edge]:
        vertex.edges = [edge for edge in vertex.edges if not edge.is_self_loop()]
        return [edge for edge in self.edges if not edge.is_self_loop()]

    def get_remaining_vertices(self) -> list[Vertex]:
        return [vertex for vertex in self.vertices if vertex is not None]

    def find_minimum_cut(self) -> int:
        while len(self.get_remaining_vertices()) > 2:
            # Pick edge at random
            random_edge = self.pick_random_edge()

            # Merge u and v into a single vertex
            merged_vertex = self.merge_vertices(random_edge)

            # remove self loops
            self.edges = self.remove_self_loops(merged_vertex)

            # print("vertices", self.vertices)
            # print("edges", self.edges)

        # print('vertices', self.vertices)
        # print('edges', self.edges)

        return len(self.edges)


total_cuts = []

for i in range(1, 100):
    random.seed(i)

    # test_edges = [
    #     Edge(1, 2),
    #     Edge(1, 3),
    #     Edge(2, 3),
    #     Edge(2, 4),
    #     Edge(3, 4),
    #     Edge(5, 2),
    #     Edge(5, 4),
    # ]

    # test_vertices = [
    #     Vertex(1, [test_edges[0], test_edges[1]]),
    #     Vertex(2, [test_edges[2], test_edges[3]]),
    #     Vertex(3, [test_edges[4]]),
    #     Vertex(4, []),
    #     Vertex(5, [test_edges[5], test_edges[6]]),
    # ]

    test_edges, test_vertices = get_edges_and_vertices()

    test_graph = Graph(test_vertices, test_edges)
    total_cuts.append(test_graph.find_minimum_cut())


print(total_cuts)
print(min(total_cuts))
