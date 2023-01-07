def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    stack = []
    paths = []
    final_index = len(graph) - 1

    initial_vert = (graph[0], [0])
    stack.append(initial_vert)

    while stack:
        vert = stack.pop()

        if vert[1][-1] == final_index:
            paths.append(vert[1])

        for new_index in vert[0]:
            new_vert = (graph[new_index], vert[1] + [new_index])
            stack.append(new_vert)

    return paths
