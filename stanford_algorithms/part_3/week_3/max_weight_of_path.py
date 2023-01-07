from typing import Optional

with open("./max_weight_input.txt") as f:
    full_input = []

    for index, line in enumerate(f):
        if index == 0:
            continue
        else:
            full_input.append(int(line))


# print(full_input)
def get_max_weight_of_path(weights: list[int]) -> list[int]:
    scores: list[Optional[int]] = [None] * (len(weights) + 1)
    scores[0] = 0
    scores[1] = weights[0]

    remaining_weights = weights[1:]

    for index, cur_weight in enumerate(remaining_weights, 2):
        if index > len(scores) - 1:
            break

        case_1 = scores[index - 1]
        case_2 = scores[index - 2] + cur_weight

        scores[index] = max(case_1, case_2)

    print("scores", scores)
    # return A
    i = len(scores) - 1

    total_weight = 0

    vertices = [0] * len(weights)

    while i >= 1:
        w_i = weights[i - 1]

        prev_score = scores[i - 1]
        cur_score = scores[i - 2] + w_i

        # print("prev score", prev_score)
        # print("cur score", cur_score)

        if prev_score >= cur_score:
            i -= 1
        else:
            vertices[i - 1] = 1
            total_weight += w_i
            i -= 2

        # print("total weight", total_weight)

    # print('total weight', total_weight)
    return vertices


test_input = [1, 3, 4, 3, 10]

# print(get)
# result = get_max_weight_of_path(test_input)
result = get_max_weight_of_path(full_input)
print(result)

for vertex in [1, 2, 3, 4, 17, 117, 517, 997]:
    print(result[vertex - 1])
