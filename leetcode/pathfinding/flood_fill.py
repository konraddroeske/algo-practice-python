def flood_fill(
    image: list[list[int]], sr: int, sc: int, color: int
) -> list[list[int]]:
    target_color = image[sr][sc]

    if target_color == color:
        return image

    def dfs(
        y: int,
        x: int,
    ) -> list[list[int]]:
        nonlocal image
        current = image[y][x]

        if current == target_color:
            image[y][x] = color

        # check up
        if y - 1 >= 0 and image[y - 1][x] == target_color:
            image = dfs(y - 1, x)

        # check down
        if y + 1 < len(image) and image[y + 1][x] == target_color:
            image = dfs(y + 1, x)

        # check right
        if x + 1 < len(image[y]) and image[y][x + 1] == target_color:
            image = dfs(y, x + 1)

        # check left
        if x - 1 >= 0 and image[y][x - 1] == target_color:
            image = dfs(y, x - 1)

        return image

    return dfs(sr, sc)


image_1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr_1 = 1
sc_1 = 1
color_1 = 2


result_1 = flood_fill(image_1, sr_1, sc_1, color_1)
for row in result_1:
    print(row)


image_2 = [[0, 0, 0], [0, 0, 0]]
sr_2 = 1
sc_2 = 0
color_2 = 2

result_2 = flood_fill(image_2, sr_2, sc_2, color_2)
for row in result_2:
    print(row)

image_3 = [[0, 0, 0], [0, 0, 0]]
sr_3 = 0
sc_3 = 0
color_3 = 0

result_3 = flood_fill(image_3, sr_3, sr_3, color_3)
for row in result_3:
    print(row)
