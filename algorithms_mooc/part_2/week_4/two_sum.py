hash_table = {}

with open("two_sum_input.txt") as f:
    for index, line in enumerate(f):
        input_val = int(line)

        if hash_table.get(input_val) is None:
            hash_table[input_val] = index

count = 0
hash_table_items = hash_table.items()

for target in range(-10000, 10001):
    for key_val, _ in hash_table_items:
        matching_val = target - key_val
        matching_pos = hash_table.get(matching_val)

        if matching_pos is not None and key_val != matching_val:
            count += 1
            break

print(count)
