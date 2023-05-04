def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(cost) > sum(gas):
        return -1

    total = 0
    start = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]

        if total < 0:
            total = 0
            start = i + 1

    return start


gas_1 = [1, 2, 3, 4, 5]
cost_1 = [3, 4, 5, 1, 2]

print(can_complete_circuit(gas_1, cost_1))

gas_2 = [2, 3, 4]
cost_2 = [3, 4, 3]

print(can_complete_circuit(gas_2, cost_2))

gas_3 = [4, 5, 2, 6, 5, 3]
cost_3 = [3, 2, 7, 3, 2, 9]

print(can_complete_circuit(gas_3, cost_3))

gas_4 = [5, 8, 2, 8]
cost_4 = [6, 5, 6, 6]

print(can_complete_circuit(gas_4, cost_4))
