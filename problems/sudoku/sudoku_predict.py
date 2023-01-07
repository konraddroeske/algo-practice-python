board = [
    [4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]

boolean_row = [[False for i in range(10)] for j in range(10)]
boolean_column = [[False for i in range(10)] for j in range(10)]
boolean_quadrant = [[False for i in range(10)] for j in range(10)]


def check_row2(number, row):
    return boolean_row[row][number]


def check_column2(number, column):
    return boolean_column[column][number]


def check_row(number, row):
    for k in range(9):
        if board[row][k] == number:
            return True

    return False


def check_column(number, column):
    for k in range(9):
        if board[k][column] == number:
            return True

    return False


def get_quadrant(row, column):
    return int((column // 3) + 1 + (row // 3) * 3)


# for row in range(9):
#     for column in range(9):
#         print(row,column,get_quadrant(row,column))
#
# row 0 1 2 = 1
#
# column 0 1 2 = 1  4  7
# column 3 4 5 = 2  5  8
# column 6 7 8 = 3  6  9

def check_quadrant2(number, row, column):
    quadrant_for_our_number = get_quadrant(row, column)
    return boolean_quadrant[quadrant_for_our_number][number]


def check_quadrant(number, row, column):
    quadrant_for_our_number = get_quadrant(row, column)

    for i in range(9):
        for j in range(9):
            if get_quadrant(i, j) == quadrant_for_our_number:
                if number == board[i][j]:
                    return True
    return False
    print()


def remove_items(coordinates_where_candidates_were_forcefully_written):
    # HERE SHOULD COME REMOVAL OF CANDIDATES
    for item in coordinates_where_candidates_were_forcefully_written:
        i, j, candidate = item
        quadrant_for_our_number = get_quadrant(i, j)
        number = candidate

        boolean_row[i][number] = False
        boolean_column[j][number] = False
        boolean_quadrant[quadrant_for_our_number][number] = False
        board[i][j] = 0
    return False


def sudoku(row, column):  # true or false
    if row == 9:
        return True
    next_row = row
    next_column = column + 1
    if next_column == 9:
        next_column = 0
        next_row = row + 1

    coordinates_where_candidates_were_forcefully_written = []

    for i in range(9):  # go through every cell in the matrix
        for j in range(9):
            if board[i][j] == 0:  # for cells that are empty
                candidates_list = []  # we will store the potential candidates for this cell in this list
                for candidate in range(1, 10):  # let's try all possible candidates
                    if check_row2(candidate, i) == False:
                        if check_column2(candidate, j) == False:
                            if check_quadrant2(candidate, i, j) == False:
                                candidates_list.append(candidate)

                # after checking each candidate
                # if len(candidates_list)==1: #if only one single candidate is possible
                #     candidate = candidates_list[0]
                #     coordinates_where_candidates_were_forcefully_written.append([i,j,candidate])
                #     board[i][j] = candidate  # take it from the list, it is at index 0
                #     boolean_row[i][candidate] = True
                #     boolean_column[j][candidate] = True
                #     quadrant_for_our_number = get_quadrant(i, j)
                #     boolean_quadrant[quadrant_for_our_number][candidate] = True

                if len(candidates_list) == 0:  # if no candidate is possible
                    remove_items(coordinates_where_candidates_were_forcefully_written)
                    return False

    #
    # #
    # for item in coordinates_where_candidates_were_forcefully_written:
    #     i,j,candidate = item
    #
    #     board[i][j] = candidate  # take it from the list, it is at index 0
    #     boolean_row[i][candidate] = True
    #     boolean_column[j][candidate] = True
    #     quadrant_for_our_number = get_quadrant(i, j)
    #     boolean_quadrant[quadrant_for_our_number][candidate] = True

    if board[row][column] != 0:
        return sudoku(next_row, next_column)

    # quadrant_for_our_number = get_quadrant(row, column)

    quadrant_for_our_number = get_quadrant(row, column)

    for number in range(1, 10):  # this goes 1 to 9
        if check_row2(number, row) == False:
            if check_column2(number, column) == False:
                if check_quadrant2(number, row, column) == False:
                    board[row][column] = number
                    boolean_row[row][number] = True
                    boolean_column[column][number] = True
                    boolean_quadrant[quadrant_for_our_number][number] = True
                    message = sudoku(next_row, next_column)
                    if message == True:
                        return True
                    boolean_row[row][number] = False
                    boolean_column[column][number] = False
                    boolean_quadrant[quadrant_for_our_number][number] = False

                    # print()
    board[row][column] = 0

    remove_items(coordinates_where_candidates_were_forcefully_written)


import time

start = time.time()

for i in range(9):
    for j in range(9):
        if board[i][j] > 0:
            boolean_row[i][board[i][j]] = True
            boolean_column[j][board[i][j]] = True
            quadrant_for_our_number = get_quadrant(i, j)
            boolean_quadrant[quadrant_for_our_number][board[i][j]] = True

sudoku(0, 0)

end = time.time()

print('time = ', end - start)

for i in range(9):
    print(board[i])

""""
board =[

[0,0,0,0,0,0,0,0,0] ,
[0,4,5,0,0,0,0,0,0] ,
[0,2,3,4,5,6,7,8,9],
[0,0,0,0,0,0,0,0,0] ,
[0,0,0,0,0,0,0,0,0] ,
[0,0,0,0,0,0,0,0,0] ,
[0,0,0,0,0,0,0,0,0] ,
[0,0,0,0,0,0,0,0,0] ,
[0,0,0,0,0,0,0,0,0] ,

]
"""
