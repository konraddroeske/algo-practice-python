# Use Kruskal's Algorithm
from collections import defaultdict
from typing import Optional


class Edge:
    def __init__(self, tail: int, head: int, distance: int) -> None:
        self.tail = tail
        self.head = head
        self.distance = distance

    def __lt__(self, obj: "Edge") -> bool:
        return self.distance < obj.distance

    def __eq__(self, obj: "Edge") -> bool:
        return self.distance == obj.distance

    def __repr__(self) -> str:
        return f"Edge(tail: {self.tail}, head: {self.head}, distance: {self.distance})"


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_node(self, edge: Edge) -> None:
        self.graph[edge.tail].append(edge.head)
        self.graph[edge.head].append(edge.tail)

    def is_cycle(self, edge: Edge) -> bool:
        start = edge.tail
        target = edge.head

        stack = [start]
        visited = set()

        while stack:
            cur_node = stack.pop()
            visited.add(cur_node)

            if cur_node == target:
                return True

            for neighbour in self.graph[cur_node]:
                if neighbour not in visited:
                    stack.append(neighbour)

        return False


input_edges = []
# input_clusters = [2, 3, 4]
input_clusters = [4]

with open("clustering_input.txt") as f:
    for index, line in enumerate(f):
        split_line = [int(val) for val in str.split(line)]

        if index == 0:
            input_nodes = split_line[0]
        else:
            input_tail = split_line[0]
            input_head = split_line[1]
            input_distance = split_line[2]

            input_edge = Edge(input_tail, input_head, input_distance)
            input_edges.append(input_edge)


def get_max_distance(edges: list[Edge], total_nodes: int, total_clusters: int) -> int:
    sorted_edges = sorted(edges)

    tree = Graph()

    cur_clusters = total_nodes
    max_spacing = None

    for edge in sorted_edges:
        if cur_clusters == total_clusters - 1:
            break

        if not tree.is_cycle(edge):
            # print("adding node", edge)
            tree.add_node(edge)
            cur_clusters -= 1
            max_spacing = edge.distance

    return max_spacing


for input_cluster in input_clusters:
    max_distance = get_max_distance(input_edges, input_nodes, input_cluster)
    print(f"cluster size: {input_cluster}")
    print(f"max distance: {max_distance}")
    print("")
