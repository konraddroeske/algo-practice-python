with open("dijkstra_data.txt") as f:
    input_vertices = []

    for line in f:
        split_line = str.split(line)

        new_edges = []

        for vals in split_line[1:]:
            (input_vertex, input_distance) = str.split(vals, ",")
            new_edges.append((int(input_vertex), int(input_distance)))

        input_vertices.append(new_edges)
#
# print(all_vertices)

# input_vertices = [
#     [(2, 1), (3, 4)],
#     [(3, 2), (4, 6)],
#     [(4, 3)],
#     [],
# ]


def dijkstra(graph: list[list[tuple[int, int]]]) -> dict[int, int]:
    start = graph[0]

    x: dict[int, list[tuple]] = {1: start}

    v: dict[int, list[tuple]] = {
        index + 1: vertex for index, vertex in enumerate(graph)
    }

    # print(x)
    # print(v)

    a: dict[int, int] = {1: 0}

    while x != v:
        # amount all edges (u, v) in x, with v not in x
        outside_edges: list[tuple[int, int, int]] = []

        for tail, edges in x.items():
            for (head, cur_distance) in edges:
                if x.get(head) is None:
                    # print("outside head", head)
                    prev_distance = a.get(tail)

                    if prev_distance is None:
                        # print("can't get prev distance")
                        break

                    new_distance = cur_distance + prev_distance
                    outside_edges.append((tail, head, new_distance))

        # print("outside edges", outside_edges)

        min_edge = min(outside_edges, key=lambda outside_edge: outside_edge[2])
        # print("min edge", min_edge)

        (tail, head, distance) = min_edge

        x[head] = graph[head - 1]
        a[head] = distance

        # print("new x", x)
        # print("cur v", v)

        # break

    return a


d = dijkstra(input_vertices)

# 7,37,59,82,99,115,133,165,188,197

print(f"{d[7],d[37],d[59],d[82],d[99],d[115],d[133],d[165],d[188],d[197]}")
