graph = {}

with open("prims_input.txt") as f:
    for index, line in enumerate(f):
        split_line = [int(val) for val in str.split(line)]

        if index == 0:
            num_nodes = split_line[0]
            num_edges = split_line[1]
        else:
            input_tail = split_line[0]
            input_head = split_line[1]
            input_cost = split_line[2]

            vertex_tail = graph.get(input_tail)
            vertex_head = graph.get(input_head)

            if vertex_tail is None:
                graph[input_tail] = [(input_head, input_cost)]
            else:
                graph[input_tail].append((input_head, input_cost))

            if vertex_head is None:
                graph[input_head] = [(input_tail, input_cost)]
            else:
                graph[input_head].append((input_tail, input_cost))

# print(graph)


def get_cheapest_edge(x: dict[int, list[tuple[int, int]]]) -> tuple[int, int, int]:
    tails = x.keys()
    result = None

    for tail in tails:
        for (head, cost) in x[tail]:
            if result is None or (x.get(head) is None and cost < result[2]):
                result = (tail, head, cost)

    if result is None:
        raise TypeError("Result cannot be None")

    return result


def prims_algorithm(v: dict[int, list[tuple[int, int]]]) -> int:
    x: dict[int, list[tuple[int, int]]] = {1: v[1]}
    t: list[tuple[int, int, int]] = []

    while x != v:
        # tail, head, cost = get_cheapest_edge(x)
        cheapest_edge = get_cheapest_edge(x)
        print(f"Cheapest edge: {cheapest_edge}")
        t.append(cheapest_edge)

        _, head, _ = cheapest_edge
        new_node = v.get(head)

        if new_node:
            x[head] = v[head]
        else:
            v[head] = []
            x[head] = []

        # print(f"New node: {head}")
        # print(len(v), len(x))

    return sum(edge[2] for edge in t)


# print(prims_algorithm(graph))
total_cost = prims_algorithm(graph)

print('Total cost:', total_cost)
