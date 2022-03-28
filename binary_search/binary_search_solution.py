# search for item in a sequence
# keep splitting list until item is found

def binary_search(sequence: list, item: int):
    # set initial indexes to beginning and end of list
    begin_index = 0
    end_index = len(sequence) - 1

    # while begin index is less than or equal to end index
    while begin_index <= end_index:
        # find midpoint index, from begin index plus half of difference
        # of beginning and end indexes
        midpoint_index = begin_index + (end_index - begin_index) // 2

        # get the midpoint value
        midpoint_value = sequence[midpoint_index]

        # if midpoint is equal to item, return midpoint value
        if midpoint_value == item:
            return midpoint_index

        # if item is less midpoint, set end index to midpoint index - 1
        elif item < midpoint_value:
            end_index = midpoint_index - 1

        # else set begin index to midpoint + 1
        else:
            begin_index = midpoint_index + 1

    # otherwise return None
    return None


seq_a = [2, 3, 4, 5, 6, 6, 7, 12]

item_a = 12

print(binary_search(seq_a, 8))

# Algorithm Complexity

# Space
# n = len(seq)
# k = # of steps
# n * 1/2 * 1/2 * ... = n / 2^k
# k = log 2 n
