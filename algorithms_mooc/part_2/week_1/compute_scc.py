# Compute SCCs of Graph
from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, label: int, neighbours: list[int]) -> None:
        self.label = label
        self.neighbours = neighbours

        self.leader: Optional[int] = None
        self.finishing_time = 0

    def __repr__(self) -> str:
        return (
            f"Node(Label: {self.label}, Finishing Time: {self.finishing_time}, Leader:"
            f" {self.leader}, Neighbours: {self.neighbours}"
        )


with open("scc_input_test.txt") as f:
    graph_dict: dict[int, Node] = {}
    rev_graph_dict: dict[int, Node] = {}

    max_val = 1

    for line in f:
        vals = [int(x) for x in str.split(line)]

        head = vals[0]
        tail = vals[1]

        if head > max_val:
            max_val = head

        if tail > max_val:
            max_val = tail

        orig_node = graph_dict.get(head)

        if orig_node:
            orig_node.neighbours.append(tail)
        else:
            graph_dict[head] = Node(head, [tail])

        rev_node = rev_graph_dict.get(tail)

        if rev_node:
            rev_node.neighbours.append(head)
        else:
            rev_graph_dict[tail] = Node(tail, [head])

    # print(max_val_orig)
    # print(max_val_rev)
    # print(max_val)

    test_graph: list[Optional[Node]] = [None] * max_val
    test_graph_rev: list[Optional[Node]] = [None] * max_val

    for key, value in graph_dict.items():
        test_graph[key - 1] = value

    for key, value in rev_graph_dict.items():
        test_graph_rev[key - 1] = value

    # for index, node in enumerate(test_graph):
    #     if node is None:
    #         test_graph[index] = Node(index + 1, [])
    #
    # for index, node in enumerate(test_graph_rev):
    #     if node is None:
    #         test_graph_rev[index] = Node(index + 1, [])

# print(test_graph)
# test_graph = [
#     Node(1, [4]),
#     Node(2, [8]),
#     Node(3, [6]),
#     Node(4, [7]),
#     Node(5, [2]),
#     Node(6, [9]),
#     Node(7, [1]),
#     Node(8, [5, 6]),
#     Node(9, [3, 7]),
# ]
#
# test_graph_rev = [
#     Node(1, [7]),
#     Node(2, [5]),
#     Node(3, [9]),
#     Node(4, [1]),
#     Node(5, [8]),
#     Node(6, [3, 8]),
#     Node(7, [9, 4]),
#     Node(8, [2]),
#     Node(9, [6]),
# ]

finishing_times: list[Optional[int]] = [None] * (len(test_graph_rev))
t = 0
s = None


def dfs_first_pass(
    visited: set[int], graph: list[Optional[Node]], node_label: int
) -> None:
    global t
    visited.add(node_label)

    reverse_node = graph[node_label - 1]

    for neighbour in reverse_node.neighbours:
        if neighbour not in visited:
            dfs_first_pass(visited, graph, neighbour)

    t += 1
    test_graph[node_label - 1].finishing_time = t


def dfs_first_pass_stack(
    visited: set[int], graph: list[Optional[Node]], start: int
) -> None:
    global t

    stack = [graph[start - 1]]
    count_stack = []

    while stack:
        reverse_node = stack.pop()
        count_stack.append(reverse_node)

        visited.add(reverse_node.label)

        for neighbour in reverse_node.neighbours:
            if neighbour not in visited:
                neighbour_node = graph[neighbour - 1]

                if neighbour_node:
                    stack.append(graph[neighbour - 1])
                else:
                    graph[neighbour - 1] = Node(neighbour, [])
                    stack.append(graph[neighbour - 1])

    while count_stack:
        count_node = count_stack.pop()
        t += 1

        finishing_node = test_graph[count_node.label - 1]

        if finishing_node:
            test_graph[count_node.label - 1].finishing_time = t
        else:
            test_graph[count_node.label - 1] = Node(count_node.label, [])
            test_graph[count_node.label - 1].finishing_time = t


def dfs_loop_first_pass(graph: list[Optional[Node]]) -> None:
    visited = set()

    for _, reverse_node in enumerate(reversed(graph)):
        if reverse_node is not None and reverse_node.label not in visited:
            dfs_first_pass_stack(visited, graph, reverse_node.label)


def dfs_second_pass(visited: set[int], graph: list[Optional[Node]], node_label: int):
    global s

    visited.add(node_label)
    original_node = graph[node_label - 1]
    original_node.leader = s

    for neighbour in original_node.neighbours:
        if neighbour not in visited:
            dfs_second_pass(visited, graph, neighbour)


def dfs_second_pass_stack(visited: set[int], graph: list[Optional[Node]], start: int):
    stack = [graph[start - 1]]
    global s

    while stack:
        original_node = stack.pop()
        original_node.leader = s

        visited.add(original_node.label)

        for neighbour in original_node.neighbours:
            if neighbour not in visited:
                stack.append(graph[neighbour - 1])


def dfs_loop_second_pass(graph: list[Node]) -> None:
    global s

    visited = set()
    sorted_by_finishing_time = sorted(
        graph, key=lambda x: x.finishing_time, reverse=True
    )

    for finishing_time_node in sorted_by_finishing_time:
        if finishing_time_node.label not in visited:
            s = finishing_time_node.finishing_time
            dfs_second_pass_stack(visited, graph, finishing_time_node.label)


dfs_loop_first_pass(test_graph_rev)
dfs_loop_second_pass(test_graph)


leaders = defaultdict(lambda: 0)

for node in test_graph:
    leaders[node.leader] += 1

result = sorted([(k, v) for k, v in leaders.items()], key=lambda x: x[1],
                reverse=True)[:5]
print(result)
